

icons = Label(frame_corpo, image=imagem,  bg=fundo)
icons.place(x=160, y=50)

descricao = Label(frame_corpo, text="Ensolarado ", anchor="center", bg=fundo, fg=cor1, font=("Arial 10"))
descricao.place(x=170, y=190)

imagem = Image.open("D:/Curso Python/projetos/icons/nuvem noite.png")
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)

icons = Label(frame_corpo, image=imagem,  bg=fundo)
icons.place(x=160, y=50)
descricao = Label(frame_corpo, text="Nublado", anchor="center", bg=fundo, fg=cor1, font=("Arial 10"))
descricao.place(x=170, y=190)


imagem = Image.open("D:/Curso Python/projetos/icons/lua.png")
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)

icons = Label(frame_corpo, image=imagem,  bg=fundo)
icons.place(x=160, y=50)
descricao = Label(frame_corpo, text="nuvem noite", anchor="center", bg=fundo, fg=cor1, font=("Arial 10"))
descricao.place(x=170, y=190)

imagem = Image.open("D:/Curso Python/projetos/icons/nuvem dia.png")
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)

icons = Label(frame_corpo, image=imagem,  bg=fundo)
icons.place(x=160, y=50)
descricao = Label(frame_corpo, text="Nublado", anchor="center", bg=fundo, fg=cor1, font=("Arial 10"))
descricao.place(x=170, y=190)