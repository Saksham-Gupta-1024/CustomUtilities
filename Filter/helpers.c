#include "./helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int k = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue)/3.0);

            image[i][j].rgbtRed = k;
            image[i][j].rgbtGreen = k;
            image[i][j].rgbtBlue = k;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE swap;
    for (int i = 0; i < height; i++)
    {
    for (int j = 0; j < width/2; j++)
    {
        swap = image[i][j];
        image[i][j] = image[i][width - j - 1];
        image[i][width - j - 1] = swap;
    }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
     RGBTRIPLE original[height][width];
    int radius = 1;

    // Create a copy of the original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            original[i][j] = image[i][j];
        }
    }

    for (int x = 0; x < height; x++)
    {
        for (int y = 0; y < width; y++)
        {
            int red_sum = 0, green_sum = 0, blue_sum = 0;
            int pixel_count = 0;

            for (int dx = -radius; dx <= radius; dx++)
            {
                for (int dy = -radius; dy <= radius; dy++)
                {
                    int new_x = x + dx;
                    int new_y = y + dy;

                    // Check if the neighboring pixel is within the image boundaries
                    if (new_x >= 0 && new_x < height && new_y >= 0 && new_y < width)
                    {
                        red_sum += original[new_x][new_y].rgbtRed;
                        green_sum += original[new_x][new_y].rgbtGreen;
                        blue_sum += original[new_x][new_y].rgbtBlue;
                        pixel_count++;
                    }
                }
            }

            image[x][y].rgbtRed = round((float)red_sum / pixel_count);
            image[x][y].rgbtGreen = round((float)green_sum / pixel_count);
            image[x][y].rgbtBlue = round((float)blue_sum / pixel_count);
        }
    }
    return;
}


// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE original[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)

        {
            original[i][j] = image[i][j];
        }
    }


       int Gx[3][3] = {{-1, 0, 1},
                    {-2, 0, 2},
                    {-1, 0, 1}};

    int Gy[3][3] = {{-1, -2, -1},
                    {0, 0, 0},
                    {1, 2, 1}};

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int GxRed = 0, GxGreen = 0, GxBlue = 0;
            int GyRed = 0, GyGreen = 0, GyBlue = 0;

            for (int k = -1; k <= 1; k++)
            {
                for (int l = -1; l <= 1; l++)
                {
                    int row = i + k;
                    int col = j + l;

                    // Handle edge cases by checking boundary conditions
                    if (row >= 0 && row < height && col >= 0 && col < width)
                    {
                        GxRed += original[row][col].rgbtRed * Gx[k + 1][l + 1];
                        GxGreen += original[row][col].rgbtGreen * Gx[k + 1][l + 1];
                        GxBlue += original[row][col].rgbtBlue * Gx[k + 1][l + 1];

                        GyRed += original[row][col].rgbtRed * Gy[k + 1][l + 1];
                        GyGreen += original[row][col].rgbtGreen * Gy[k + 1][l + 1];
                        GyBlue += original[row][col].rgbtBlue * Gy[k + 1][l + 1];
                    }
                }
            }

            int red = round(sqrt(GxRed * GxRed + GyRed * GyRed));
            int green = round(sqrt(GxGreen * GxGreen + GyGreen * GyGreen));
            int blue = round(sqrt(GxBlue * GxBlue + GyBlue * GyBlue));

            image[i][j].rgbtRed = (unsigned char)(red > 255 ? 255 : red);
            image[i][j].rgbtGreen = (unsigned char)(green > 255 ? 255 : green);
            image[i][j].rgbtBlue = (unsigned char)(blue > 255 ? 255 : blue);
        }
    }
}