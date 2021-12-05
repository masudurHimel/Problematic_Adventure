class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.org = image[sr][sc]
        self.dfs(image, sr, sc, newColor)
        return image

    def dfs(self, image, r, c, newColor):
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
            return
        if image[r][c] == newColor:
            return
        elif image[r][c] == self.org:
            image[r][c] = newColor

            self.dfs(image, r + 1, c, newColor)
            self.dfs(image, r - 1, c, newColor)
            self.dfs(image, r, c + 1, newColor)
            self.dfs(image, r, c - 1, newColor)