/**
 * Copies a BMP piece by piece, just because.
 */
//  implement a program that reveals a hidden message in a BMP
#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

// TODO
// open file clue.bmp
// update header's info for output file verdict.bmp
// read clue's scanline, pixel by pixel
// change pixel's color as necessary to reveal the hidden clue
// write verdict's scanline, pixel by pixel

// the function excepts exactly two arguments.
// 1) the name of an input file to open for reading
// 2) followed by the name of an output file to open for writing.
// example: ./whodunit clue.bmp verdict.bmp
int main(int argc, char *argv[])
{
    // ensure proper usage
    // If your program is executed with fewer or more than two command-line arguments,
    // it should remind the user of correct usage, as with fprintf (to stderr), and main should return 1.
    if (argc != 3)
    {
        fprintf(stderr, "Usage: ./copy infile outfile\n");
        return 1;
    }

    // remember filenames
    char *infile = argv[1];
    char *outfile = argv[2];

    // open input file clue.bmp for reading
    FILE *inptr = fopen(infile, "r");
    // If the input file cannot be opened for reading, your program should inform the user as much,
    // as with fprintf (to stderr), and main should return 2.
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // open output file verdict.bmp for writing.
    FILE *outptr = fopen(outfile, "w");
    // If the output file cannot be opened for writing, your program should inform the user as much,
    // as with fprintf (to stderr), and main should return 3.
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf; // The BITMAPFILEHEADER structure contains information about the type, size, and layout of a file that contains a DIB.
    // read clue's scanline, pixel by pixel
    // fread(data, size, number, inptr);
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi; // The BITMAPINFOHEADER structure contains information about the dimensions and color format of a DIB.
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    // If the input file is not a 24-bit uncompressed BMP 4.0, your program should inform the user as much,
    // as with fprintf (to stderr), and main should return 4.
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    // write outfile's BITMAPFILEHEADER
    // wirte verdict's scanline, pixel by pixel
    // write(data, size, number, outptr)
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // determine padding for scanlines
    int padding =  (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    // iterate over infile's scanlines
    for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++) // abs - computes absolute value. Always returns a positive value. Returns x if x is positive and -x if x is negative.
    {
        // iterate over pixels in scanline
        for (int j = 0; j < bi.biWidth; j++)
        {
            // temporary storage
            RGBTRIPLE triple; // The RGBTRIPLE structure describes a color consisting of relative intensities of red, green, and blue. The bmciColors member of the BITMAPCOREINFO structure consists of an array of RGBTRIPLE structures.

            // read RGB triple from infile
            // fread(data, size, number, outptr)
            fread(&triple, sizeof(RGBTRIPLE), 1, inptr);
            // remove all full red pixels by making them black
            if (triple.rgbtRed == 255)
            {
        		triple.rgbtRed = 0;
          		triple.rgbtBlue = 0;
        		triple.rgbtGreen = 0;
            }
            // write RGB triple to outfile
            // change pixel's color as necessary to reveal the hidden clue
            fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
        }

        // skip over padding, if any
        // fseek(inptr, offset, from)
        fseek(inptr, padding, SEEK_CUR); // file position indicator

        // then add it back (to demonstrate how)
        for (int k = 0; k < padding; k++)
        {
            // here we are putting padding into our verdict.bmp output file
            fputc(0x00, outptr); // 0x00 is padding
        }
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    // Upon success, main should 0
    return 0;
}
