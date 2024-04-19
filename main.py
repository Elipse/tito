import arrr
from pyscript import document


def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = arrr.translate(english)
    program = 'suma = 10 + 29'   
    exec(program) 
    print(globals())
    print(locals())
    print('ess4', locals()['suma'])
    output_div.innerText = locals()['suma']
    

