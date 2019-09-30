import discord
from discord.ext import commands
import typing
import random

'''
All the of inside jokes my personal friends poke fun at.
# jam: His classic quote, only you get to choose who he directs it to
# taka: Random quotes from our friend taka
# carlos: members kept trying to use our other friend's names as commands so I made this
          to let them know it doesn't exist yet
'''
class Council(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['j','jamarie','jama'])
    async def jam(self, ctx, *, person):
    	responses = ['playing Xenoblade.', 'working for Square Enix',
    				 'beating Dante in Tekken.', 'being 6"1.', 'becoming the President.',
    				 'applying for NASA.', 'becoming a singer.', 'marrying Yuna.', 'baking cakes.'
    				 'skatboarding.', 'being a porn star.', 'playing at the Olympics.', 'being an Uber driver.',
    				 'in the NBA.', 'being a fry cook.', 'flipping burgers.', 'skydiving.', 'playing Tekken.',
    				 'beating Al in Tekken.', 'bodying Taka in Tekken.', 'beating JDCR in Tekken.', 'playing Smash Ultimate.',
    				 'gaining the upper hand.', 'beating Thanos.', 'being a surgeon.', 'being a WWE superstar.', 'playing Blitzball.',
    				 'attaining the Key blade.', 'riding a mech.', 'vanquishing evil.', 'drawing anime.', 'having a foot fetish.',
    				 'being friendly with Riku.', 'throwing hands with Tidus.', 'going to the gym with Waka.', 'killing his entire clan.',
    				 'saving his friends.', 'in FALCOMHIVE.', 'baking bread.', 'smoking the nut pack with me.', 'being my weed dealer.',
    				 'beating Calamity.','chilling out with Noctis.', 'joining the Organization XIII', 'joining the Free Masons.', 'listening to 2-pack.',
    				 'going skydiving.', 'marrying Terra from FF6.', 'finding the One Piece.', 'taking out the trash.', 'commiting suicide.', 'throwing hands.',
    				 'catching them all.', 'being a pokemon master', 'fucking his friend\'s mom.', 'reading.', 'stoping Shinra\'s plans.', 'building a gunpla.', 'refusing to eat breakfast.',
    				 'forgetting the alphabet.']

    	await ctx.send(f'Y\'know what? I can see {person} {random.choice(responses)}')

    @jam.error
    async def jam_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
        	await ctx.send('Please specify a person\'s name.')

    @commands.command(aliases=['t','ta','tak'])
    async def taka(self, ctx):
        responses = ['Drip', 'Quiet', 'See me in Tekken', 'Fool', 'Cloud is Zack\'s echo fighter.', 'One some true shit.', 'Sleep', 'Join bitch',
    	             'Facts', 'Watchu mean',  'Kh1 Sora has no drip.', 'What do you mean he has drip!?', 'Sud!', 'Get this shit outta here', 'change your avi.',
    	             'Teleporting merchant', 'Watch ya lingo.', 'Cause Al don\'t got smash.', 'Stay in your lain.', 'Stfu Dante.', 'I played Alisa earlier, empty win tbh.',        	             'And anyways I ain\'t lose to em I just don\'t like them.', 'A sauceless bum.', 'Who deleted my message', 'mid', 'Armor King coller tho.',
        	         'Im stealing that fit.', 'Goku SSJ4 raw though.', 'Vegeta SSJ4 ugly af.', 'Where the call at', 'Al you play a drunk bastard.', 'FACTS CRO.',
        	         'Shutcho ass up Dante', 'Whoever deleted fuck you.', 'I learned a new ability.', 'This man Jamarie playing Toon Town in 2019',
        	         'look at Jamarie icon', 'BURH THAT MIGUEL', 'Armor King is fire', 'Dvante a wanted man now', 'All Bryan slander from me is now null and void',
        	         'Stop being a pussy.', '-___-', 'Dale', 'You smell like rotten tomatoes', 'Asuka showers everyday', 'Musty ass bitch.', 'Fake ass Kawhi Leonard',
                     'I don\'t use turtlenecks ya fool.', 'I came I fought I conquered', 'Man fixed his knee so easily', 'Y\'all got a call up without telling me???',
        	         'I\'m broke broke right now.', 'My Devil Jin is getting better :smiling_imp:', 'Dante como te sientes?', 'I want to rank up -__-',
        	         'MainMan inspired me to play Kazuya', 'Carlos stop', 'This is only for Tekken characters you retarded fuck', 'See me in the sticks.',
        	         'I want to pull up on JDCR', 'Devil Jin...he\'s ok', 'We need this bum ass mf out of the series', 'We need some fathers in this community.', 'Btw, mental health ain\'t no joke.',
        	         'We know you from America.', 'Why you so angry Al.', 'You play Katarina and Armor King, pick a disability', 'I\'ll kill you', 'Don\'t talk to my brother like that',
        	         'Did I stutter?', 'You\'ve breath your last Al', 'How am I simp?', 'And you play Katarina']

        await ctx.send(random.choice(responses))

    @commands.command(aliases=['c', 'cro', 'faisal', 'matt', 'dante'])
    async def carlos(self, ctx, *, anything):
        await ctx.send('this is not a fucking command')

    @carlos.error
    async def carlos_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('This is not a command. Fuck off.')

def setup(client):
    client.add_cog(Council(client))
