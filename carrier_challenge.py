import pandas as pd 


class Carriers():
    def __init__(self, archive_path):
        self.archive = pd.read_csv(archive_path)

    def shipping(self, city, weight):
        carriers_for_city = self.archive.loc[self.archive['Cidade']==city]
        if not carriers_for_city.empty:
            if weight<=100:
                rapid = self.localize(carriers_for_city, 'Tempo para Entrega')
                cheap = self.localize(carriers_for_city, 'Custo de Frete até 100Kg [R$/Kg]')
                
                return [
                    [cheap[' Nome'].iloc[0], weight, city, cheap['Custo de Frete até 100Kg [R$/Kg]'].iloc[0], cheap['Tempo para Entrega'].iloc[0]],
                    [rapid[' Nome'].iloc[0], weight, city, rapid['Custo de Frete até 100Kg [R$/Kg]'].iloc[0], rapid['Tempo para Entrega'].iloc[0]]
                ]

            else:
                rapid = self.localize(carriers_for_city, 'Tempo para Entrega')
                cheap = self.localize(carriers_for_city, 'Custo de Frete mais de 100Kg [R$/Kg]')
                
                return [
                    [cheap[' Nome'].iloc[0], weight, city, cheap['Custo de Frete mais de 100Kg [R$/Kg]'].iloc[0], cheap['Tempo para Entrega'].iloc[0]],
                    [rapid[' Nome'].iloc[0], weight, city, rapid['Custo de Frete mais de 100Kg [R$/Kg]'].iloc[0], rapid['Tempo para Entrega'].iloc[0]]
                ]  
        else:
            return [city]
    
    def localize(self, dataframe, key):
        if len(pd.to_numeric(self.string_to_numeric(dataframe[key])))>1: 
            minimum = min(pd.to_numeric(self.string_to_numeric(dataframe[key])))
        else:
            return dataframe.loc[dataframe[key] == dataframe[key]]
        
        if key == 'Tempo para Entrega':
            minimum = str(minimum)+'h'
        else:    
            minimum = ('R$ '+ str(minimum))
        return dataframe.loc[dataframe[key] == minimum]
        
    def string_to_numeric(self, strings):
        strings = list(strings)
        result=[]
        
        for s in strings:
            if 'h' in s:
                result.append(s[:-1])
            elif 'R$' in s:
                result.append(s[2:])

        return result