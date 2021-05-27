from carrier_challenge import Carriers

class Test():
    def show_less_than_100(self, less_than_100):
        if less_than_100:
            print( "A transportadora {} eh a mais barata para entregar produtos com menos de 100KG em {}".format(
                                                                                                        less_than_100[0][0],
                                                                                                        less_than_100[0][2]
                                                                                                    ))
            print("Valor = {} | Peso = {}Kg | Tempo de Entrega = {}".format(less_than_100[0][3], less_than_100[0][1],less_than_100[0][4]))
            print("\n")
            print("A transportadora {} eh a mais rapida para entregar produtos com menos de 100KG em {}".format(
                                                                                                                less_than_100[1][0],
                                                                                                                less_than_100[1][2]
                                                                                                            ))
            print("Valor = {} | Peso = {}Kg | Tempo de Entrega = {}".format(less_than_100[1][3],less_than_100[1][1],less_than_100[1][4]))
            print("\n")
        else:
            print("Nao ha informacoes de envio para essa cidade {}".format(more_than_100[0]))

    def show_more_than_100(self, more_than_100):
        if len(more_than_100)>1:
            print( "A transportadora {} eh a mais barata para entregar produtos com mais de 100KG em {}".format(
                                                                                                        more_than_100[0][0],
                                                                                                        more_than_100[0][2]
                                                                                                    ))
            print("Valor = {} | Peso = {}Kg | Tempo de Entrega = {}".format(more_than_100[0][3], more_than_100[0][1],more_than_100[0][4]))
            print("\n")
            print("A transportadora {} eh a mais rapida para entregar produtos com mais de 100KG em {}".format(
                                                                                                                more_than_100[1][0],
                                                                                                                more_than_100[1][2]
                                                                                                            ))
            print("Valor = {} | Peso = {}Kg | Tempo de Entrega = {}".format(more_than_100[1][3],more_than_100[1][1],more_than_100[1][4]))
            print("\n")
        else:
            print("Nao ha informacoes de envio para essa cidade {}".format(more_than_100[0]))

test_obj = Test()
carrier_obj = Carriers('transportadoras.csv')


less_than_100 = carrier_obj.shipping("São Paulo", 10.1)
more_than_100 = carrier_obj.shipping("Campinas", 101)

test_obj.show_less_than_100(less_than_100)
test_obj.show_more_than_100(more_than_100)

