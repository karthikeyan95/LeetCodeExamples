from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        current_color = image[sr][sc]
        new_image = self.fillImage(image, sr, sc, newColor, current_color)
        return new_image

    def fillImage(self, image: List[List[int]], sr: int, sc: int, newColor: int, current_color: int) -> List[List[int]]:
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] == newColor or \
                image[sr][sc] != current_color:
            return image
        image[sr][sc] = -10
        image = self.fillImage(image, sr + 1, sc, newColor, current_color)
        image = self.fillImage(image, sr - 1, sc, newColor, current_color)
        image = self.fillImage(image, sr, sc + 1, newColor, current_color)
        image = self.fillImage(image, sr, sc - 1, newColor, current_color)
        return image


def main():
    # image = [[1,1,1],[1,1,0],[1,0,1]]
    image = [[0, 0, 0], [0, 1, 1]]
    sr = 1
    sc = 1
    new_color = 1
    obj = Solution()
    print(obj.floodFill(image, sr, sc, new_color))


if __name__ == '__main__':
    main()

