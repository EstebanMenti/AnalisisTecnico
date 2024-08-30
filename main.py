import os
import datetime as date 
import sys
import argparse
import yfinance as yf
from graficos import grafico_fundamental as gf
from graficos import graficos

def main(period, tickers=''):

    print("***********************************************************************")
    print("***********************************************************************")
    formato = "%d-%m-%Y %H:%M:%S"
    print("Inicio del programa: ", date.datetime.today().strftime(formato)+"\n")
    
    try:
        tickers  = yf.Tickers(tickers)  
    except:
        print("Error en bajar datos")
    
    history = get_history(tickers, period=period)
    graficos(history, dato='Close')

    normalizado = get_normalizado(history, dato='Close')  
    graficos(normalizado, dato='percent')
        
def get_history( tickers, period ):
    # Diccionario para almacenar los datos de precios históricos
    tickers_data = {}
    
    for symbol in tickers.tickers:
        try:
            # Descargar datos históricos para el símbolo
            data = tickers.tickers[symbol].history(period=period)
            
            # Verificar si los datos están vacíos
            if not data.empty:
                tickers_data[symbol] = data
        except Exception as e:
            print(f"Error al obtener datos para {symbol}: {e}")
    
    return tickers_data
    
    
    print("Hola Mundo") 

def get_normalizado( dic, dato='close' ):
    for key in list(dic):
        #dic[key]['percent'] = (dic[key][dato] / dic[key][dato][0]) * 100
        dic[key]['percent'] = (dic[key][dato] / dic[key][dato].iloc[0]) * 100
    return( dic )   


# Verifica si este archivo está siendo ejecutado directamente
if __name__ == "__main__":
    #Limpia la pantalla (para Windows)
    os.system ("cls")

    # Crear el parser de argumentos
    parser = argparse.ArgumentParser(description="VER 0.1. Debe pasar parametros al main para procesar los datos")

    # Definir los argumentos con nombres
    parser.add_argument("--t", required=True, nargs='+', help="Listado de Acciones (ej: AAPL AMD)")
    parser.add_argument("--p", required=False, default="5Y", help="Periodo a analizar (1d, 1S, 1mo, 1Y). Por defecto 5Y (5 años)")

    try:
        # Parsear los argumentos
        args = parser.parse_args()
        main(tickers= args.t,  period=args.p)
    except argparse.ArgumentError as e:
        print(f'Error en el argumento: {e}')
    except SystemExit as e:
        print(f'Error: El argumento "--a es requerido. Favor de proporcione un valor')
        sys.exit(1) 