class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for img in image:
            # img=img[::-1]
            img.reverse()
        for img in image:
            for idx in range(len(img)):
                if img[idx]:
                    img[idx]=0
                else:
                    img[idx]=1
        return image