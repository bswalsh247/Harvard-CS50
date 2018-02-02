/**
 * Copies a BMP piece by piece, just because.
 * Implement a program called resize that resizes (i.e., enlarges) 24-bit uncompressed BMPs by a factor of n.
 * Uses the "rewrite" method (remembers pixels in an array and writes array as many times as needed)
 */

#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: ./resize n infile outfile\n");
        return 1;
    }

    // factor for resizing the image
    int n = atoi(argv[1]);

    // the first (n) must be a positive integer less than or equal to 100
    if (n < 1 || n > 100)
    {
        printf("BPM factor (n) for resizing must be a positive int less than or equal to 100\n");
        return 2;
    }

    // remember filenames
    char *infile = argv[2];
    char *outfile = argv[3];

    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 3;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 4;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 5;
    }

    // variables for old biWidth (in pixels), biHeight (in pixels), padding (in bytes)
    int old_biWidth = bi.biWidth;
    int old_biHeight = bi.biHeight;
    int old_padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    // variables for new biWidth (in pixels), biHeight (in pixels), padding (in bytes)
    bi.biWidth *= n;
    bi.biHeight *= n;
    int new_padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    // update biSizeImage for new image size (in bytes).
    bi.biSizeImage = ((bi.biWidth * sizeof(RGBTRIPLE)) + new_padding) * abs(bi.biHeight);

    // update bfSize for new size of file (in bytes). Includes pixels, padding, and headers
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // dynmaically allocate memory from the heap to hold scanline
    RGBTRIPLE *array = malloc(sizeof(RGBTRIPLE) * (bi.biWidth));

    // read infile's scanline, pixel by pixel
    // iterate over infile's scanlines
    for (int i = 0, biHeight = abs(old_biHeight); i < biHeight; i++)
    {
        int tracker = 0;
        // iterate over pixels in scanline
        for (int j = 0; j < old_biWidth; j++)
        {
            // temporary storage
            RGBTRIPLE triple;

            // read RGB triple from infile
            // fread(data, size, number, inptr)
            fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

            // write pixel to array n times
            for (int counter = 0; counter < n; counter++)
            {
                *(array + (tracker)) = triple;
                tracker++;
            }
        }

        // skip over padding, if any
        fseek(inptr, old_padding, SEEK_CUR);

        // write RGB triple to outfile
        for (int l = 0; l < n; l++)
        {
            fwrite((array), sizeof(RGBTRIPLE), bi.biWidth, outptr);

            // then add it back (to demonstrate how)
            for (int k = 0; k < new_padding; k++)
            {
                fputc(0x00, outptr);
            }
        }

    }
    // free memory from heap
    free(array);

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
