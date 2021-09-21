game = {
    #copy this 
    'blank': {
        'dialogue': [],
        'prompt': '',
        'options': [],
        'switch': {
            '': '',
            '': ''
        }
    },
    #till here and fill in the blanks, whenever you want to add something
    'start': {
        'dialogue': ["This is an example of dialogue", "There can be muliple"],#dialogue goes here
        'prompt': 'Did you understand this? [a) yes / b) no]',#this is what the user will be prompted with
        'options': ['a', 'b'],#the valid input 
        'switch': {#where each option takes you
            'a': 'start',# if user enters 'a' it takes them to start
            'b': 'start'# if user enters 'b' it takes them to start
        }
    }

}