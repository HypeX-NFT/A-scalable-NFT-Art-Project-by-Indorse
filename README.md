# A-scalable-NFT-Art-Project-by-Indorse

1. Web crawled the cyperpunk 2077 and other exotic photos with similar style fashions to our product as the background for Generative Adversarial Network model.
2. Used the pretrained-CycleGAN model to fuse the generate background from our web-scrapped cyperpunk background.
3. Overlapped our product with the chosen background and then used the randomly generated ID to set the color grading for our background photo.
  - Common: 57%
  - Rare: 30%
  - Epic: 10%
  - Legendary: 3%
4. Based on the randomly generated ID, we differentiated the rarity of each product-background pair.


# Interface with Backend on Rarible/Circle API/IPFS
input: 
- Path
- string: e.g. userID + System.time()

output:
- Photo: Text + Product + Frame + Background (After CycleGan) + Encoding
