from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Custom Menssage"

@app.route('/bug')                                                                                                                                
def bad():                                                                                                                                        
    try:                                                                                                                                          
        raise TypeError()                                                                                                                         
    except TypeError as e:                                                                                                                        
        print(e)                                                                                                                                  
    except TypeError as e:                                                                                                                        
        print("Duplicado, ou seja, nunca vai entrar aqui.")  

if __name__ == '__main__':
    app.run()