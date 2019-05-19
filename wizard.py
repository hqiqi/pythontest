from spell import Spell
from spellbook import Spellbook

# This will show the spell and spellbook classes in action.
# There's a lot that will be printed to standard output, so feel free to comment out some sections
# to narrow the output down to the functions you want to see.

tablet = Spellbook('Stone', 24)
post_it_note = Spellbook('Paper', 3)

cat_summoned = "You reach into your pocket for a can of tuna and crack it open. A cat pops into existence beside you in a puff of smoke!"
summon = Spell("Summon Cat", "Conjuration", 1, 4, cat_summoned)

tickle = Spell('Tickle', 'Evocation', 0, 100, "You point at a target and watch them squirm as an invisible feather begins tickling at their sides! Or not. Some people aren't ticklish.")

castle = Spell("Queen Elsa's Instant Castle", 'Transmutation', 8, 1, "You sing a showstopping Broadway tune and build an ice castle out of basically nothing. That feels pretty great.")

cheesecake = Spell("Cheesecake Calamity", 'Conjuration', 8, 5, "You mutter a few words and a slice of cheesecake spontaneously appears on a point that you can see within range. Then two slices. Then four. Then eight. Sixteen. Thirty-two. Oh no...")

anti_cheesecake = Spell("Destroy Cheesecake", 'Evocation', 7, 3, "For the next five minutes, any continuous segment of cheesecake you touch immediately disintegrates. It tastes lovely.")

f_ball = Spell("Fireball", 'Evocation', 3, 3, "You crush a bit of charcoal between your fingers and specify a point within 120 feet. An explosion of heat and light (and smoke!) expands from that point, and it's just SO PRETTY.")

# Adding spells, casting spells that don't exist.

print('================ ADDING SPELLS, SPELLS NOT FOUND ================\n\n')

post_it_note.add_spell(tickle)
post_it_note.add_spell(f_ball)

try:
	post_it_note.add_spell(cheesecake)
except ValueError as e:
	print('{}\n'.format(e))

post_it_note.cast_spell("Destroy Cheesecake")
print('\n\n================ CASTING ================\n\n')
post_it_note.cast_spell("Fireball")
print('\n\n================ CAST_ALL ================\n\n')
post_it_note.cast_all()
print('\n\n================ CAST_STRONGEST ================\n\n')

tablet.add_spell(summon)
tablet.add_spell(cheesecake)
tablet.add_spell(castle)
tablet.add_spell(anti_cheesecake)

tablet.cast_strongest()				# This should cast "Elsa's Instant Castle"
print('\n\n================ CAST_STRONGEST AGAIN ================\n\n')
tablet.cast_strongest() 			# This should cast "Cheesecake Calamity"
print('\n\n================ CAST_ALL AGAIN ================\n\n')
tablet.cast_all()
print('\n\n================')
tablet.recharge_all()