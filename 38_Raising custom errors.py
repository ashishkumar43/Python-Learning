#custom error (error dunga taki aage kuch jyada galat na ho jaye )
# jaise hum mossi ko khana dene ja rhe hai aur waha par hume raste mai pata chal gya ki mummy ke sabji ka thela padka diya hai to wohi ruk jaunga aage hi bhadunga
a=int(input("Enter any value b/w 5 and 9 "))
if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")
