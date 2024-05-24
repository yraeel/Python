class Televisao:
    def __init__(self, tamanho, marca, min=None, max=None):
        self.ligada = False
        self.canal = 2
        self.tamanho = tamanho
        self.marca = marca
        
        self.min = min if min is not None else 2
        self.max = max if max is not None else 14

    

            
    
    # def muda_canal_para_baixo(self):

    #     if self.canal - 1 >= self.cmin:
    #         self.canal -= 1
        

    # def muda_canal_para_cima(self):
    #     if self.canal + 1 <= self.cmax:
    #         self.canal += 1        


tv = Televisao(25, 'sony', 1, 99)
tv_sala = Televisao(27, 'lg')

print(f'{tv.tamanho} - {tv.marca} - {tv.min} - {tv.max}')
print(f'{tv_sala.tamanho} - {tv_sala.marca} - {tv_sala.min} - {tv_sala.max}' )


