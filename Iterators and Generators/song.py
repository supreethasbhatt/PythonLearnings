'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''

def make_song(count=99,beverage='soda'):
    while count > 1:
        yield "{} bottles of {} on the wall.".format(count,beverage)
        count -= 1
    yield "Only 1 bottle of {} left!".format(beverage)
    yield "No more {}!".format(beverage)
        
for i in make_song(2):
    print(i)

