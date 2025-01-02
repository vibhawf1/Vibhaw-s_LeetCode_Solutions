class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        self.r = len(img)
        self.c = len(img[0])
        return  [[self.smooth(i,j,img) for j in range(self.c)] for i in range(self.r)]
    def smooth(self,r,c,img):
        dr = [0, 0, 0,-1, 1,-1, 1,-1, 1]
        dc = [0, 1,-1, 0, 0,-1, 1, 1,-1]
        sums = count = 0
        for i in range(9):
            rr = r + dr[i]
            cc = c + dc[i]
            if rr<0 or cc<0 or rr>=self.r or cc>=self.c:
                continue
            sums += img[rr][cc]
            count +=1
        return sums//count

        
