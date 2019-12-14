def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        print('Bonjour')
    else:
        return 'Hello'

print(greet('es'), 'Glenn')
print(str(greet('fr')) + 'Glenn')

# trying to understand the difference b/w print and return