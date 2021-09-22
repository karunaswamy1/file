banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
f=open("file-question3.txt naam","w")
# f.write("kotak\nHDFC\nRBI\nSBI\nBank of baroda\n")
for i in banks_list:
    f.write(i+"\n")
f.close()
    
    
