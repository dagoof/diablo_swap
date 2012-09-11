from coordinates import Skills, Skill, Pages
from common import attrdict

class Barbarian:
    _bash = Pages.page_0, Skill.ability_3_0
    _cleave = Pages.page_0, Skill.ability_3_1
    _frenzy = Pages.page_0, Skill.ability_3_2
    _hammer_of_the_ancients = Pages.page_1, Skill.ability_4_0
    _rend = Pages.page_1, Skill.ability_4_1
    _seismic_slam = Pages.page_1, Skill.ability_4_2
    _whirlwind = Pages.page_1, Skill.ability_4_3
    _ground_stomp = Pages.page_2, Skill.ability_4_0
    _leap = Pages.page_2, Skill.ability_4_1
    _sprint = Pages.page_2, Skill.ability_4_2
    _ignore_pain = Pages.page_2, Skill.ability_4_3
    _ancient_spear = Pages.page_3, Skill.ability_4_0
    _revenge = Pages.page_3, Skill.ability_4_1
    _furious_charge = Pages.page_3, Skill.ability_4_2
    _overpower = Pages.page_3, Skill.ability_4_3
    _weapon_throw = Pages.page_4, Skill.ability_4_0
    _threatening_shout = Pages.page_4, Skill.ability_4_1
    _battle_rage = Pages.page_4, Skill.ability_4_2
    _war_cry = Pages.page_4, Skill.ability_4_3
    _earthquake = Pages.page_5, Skill.ability_3_0
    _call_of_the_ancients = Pages.page_5, Skill.ability_3_1
    _wrath_of_the_berserker = Pages.page_5, Skill.ability_3_2

barbarian = attrdict({

    # bash
    'bash': (Barbarian._bash, Skill.rune_0),
    'clobber': (Barbarian._bash, Skill.rune_1),
    'onslaught': (Barbarian._bash, Skill.rune_2),
    'punish': (Barbarian._bash, Skill.rune_3),
    'instigation': (Barbarian._bash, Skill.rune_4),
    'pulverize': (Barbarian._bash, Skill.rune_5),

    # cleave
    'cleave': (Barbarian._cleave, Skill.rune_0),
    'rupture': (Barbarian._cleave, Skill.rune_1),
    'reaping_swing': (Barbarian._cleave, Skill.rune_2),
    'scattering_blast': (Barbarian._cleave, Skill.rune_3),
    'broad_sweep': (Barbarian._cleave, Skill.rune_4),
    'gathering_storm': (Barbarian._cleave, Skill.rune_5),

    # frenzy
    'frenzy': (Barbarian._frenzy, Skill.rune_0),
    'sidearm': (Barbarian._frenzy, Skill.rune_1),
    'triumph': (Barbarian._frenzy, Skill.rune_2),
    'vanguard': (Barbarian._frenzy, Skill.rune_3),
    'smite': (Barbarian._frenzy, Skill.rune_4),
    'maniac': (Barbarian._frenzy, Skill.rune_5),

    # hammer_of_the_ancients
    'hammer_of_the_ancients': (Barbarian._hammer_of_the_ancients, Skill.rune_0),
    'rolling_thunder': (Barbarian._hammer_of_the_ancients, Skill.rune_1),
    'smash': (Barbarian._hammer_of_the_ancients, Skill.rune_2),
    'the_devils_anvil': (Barbarian._hammer_of_the_ancients, Skill.rune_3),
    'thunderstrike': (Barbarian._hammer_of_the_ancients, Skill.rune_4),
    'birthright': (Barbarian._hammer_of_the_ancients, Skill.rune_5),

    # rend
    'rend': (Barbarian._rend, Skill.rune_0),
    'ravage': (Barbarian._rend, Skill.rune_1),
    'blood_lust': (Barbarian._rend, Skill.rune_2),
    'lacerate': (Barbarian._rend, Skill.rune_3),
    'mutilate': (Barbarian._rend, Skill.rune_4),
    'bloodbath': (Barbarian._rend, Skill.rune_5),

    # seismic_slam
    'seismic_slam': (Barbarian._seismic_slam, Skill.rune_0),
    'stagger': (Barbarian._seismic_slam, Skill.rune_1),
    'shattered_ground': (Barbarian._seismic_slam, Skill.rune_2),
    'rumble': (Barbarian._seismic_slam, Skill.rune_3),
    'strength_from_earth': (Barbarian._seismic_slam, Skill.rune_4),
    'cracking_rift': (Barbarian._seismic_slam, Skill.rune_5),

    # whirlwind
    'whirlwind': (Barbarian._whirlwind, Skill.rune_0),
    'dust_devils': (Barbarian._whirlwind, Skill.rune_1),
    'hurricane': (Barbarian._whirlwind, Skill.rune_2),
    'blood_funnel': (Barbarian._whirlwind, Skill.rune_3),
    'wind_shear': (Barbarian._whirlwind, Skill.rune_4),
    'volcanic_eruption': (Barbarian._whirlwind, Skill.rune_5),

    # ground_stomp
    'ground_stomp': (Barbarian._ground_stomp, Skill.rune_0),
    'deafening_crash': (Barbarian._ground_stomp, Skill.rune_1),
    'wrenching_smash': (Barbarian._ground_stomp, Skill.rune_2),
    'trembling_stomp': (Barbarian._ground_stomp, Skill.rune_3),
    'foot_of_the_mountain': (Barbarian._ground_stomp, Skill.rune_4),
    'avalanche': (Barbarian._ground_stomp, Skill.rune_5),

    # leap
    'leap': (Barbarian._leap, Skill.rune_0),
    'iron_impact': (Barbarian._leap, Skill.rune_1),
    'launch': (Barbarian._leap, Skill.rune_2),
    'toppling_impact': (Barbarian._leap, Skill.rune_3),
    'call_of_arreat': (Barbarian._leap, Skill.rune_4),
    'death_from_above': (Barbarian._leap, Skill.rune_5),

    # sprint
    'sprint': (Barbarian._sprint, Skill.rune_0),
    'rush': (Barbarian._sprint, Skill.rune_1),
    'run_like_the_wind': (Barbarian._sprint, Skill.rune_2),
    'marathon': (Barbarian._sprint, Skill.rune_3),
    'gangway': (Barbarian._sprint, Skill.rune_4),
    'forced_march': (Barbarian._sprint, Skill.rune_5),

    # ignore_pain
    'ignore_pain': (Barbarian._ignore_pain, Skill.rune_0),
    'bravado': (Barbarian._ignore_pain, Skill.rune_1),
    'iron_hide': (Barbarian._ignore_pain, Skill.rune_2),
    'ignorance_is_bliss': (Barbarian._ignore_pain, Skill.rune_3),
    'mob_rule': (Barbarian._ignore_pain, Skill.rune_4),
    'contempt_for_weakness': (Barbarian._ignore_pain, Skill.rune_5),

    # ancient_spear
    'ancient_spear': (Barbarian._ancient_spear, Skill.rune_0),
    'grappling_hooks': (Barbarian._ancient_spear, Skill.rune_1),
    'skirmish': (Barbarian._ancient_spear, Skill.rune_2),
    'dread_spear': (Barbarian._ancient_spear, Skill.rune_3),
    'harpoon': (Barbarian._ancient_spear, Skill.rune_4),
    'rage_flip': (Barbarian._ancient_spear, Skill.rune_5),

    # revenge
    'revenge': (Barbarian._revenge, Skill.rune_0),
    'vengeance_is_mine': (Barbarian._revenge, Skill.rune_1),
    'best_served_cold': (Barbarian._revenge, Skill.rune_2),
    'retribution': (Barbarian._revenge, Skill.rune_3),
    'grudge': (Barbarian._revenge, Skill.rune_4),
    'provocation': (Barbarian._revenge, Skill.rune_5),

    # furious_charge
    'furious_charge': (Barbarian._furious_charge, Skill.rune_0),
    'battering_ram': (Barbarian._furious_charge, Skill.rune_1),
    'merciless_assault': (Barbarian._furious_charge, Skill.rune_2),
    'stamina': (Barbarian._furious_charge, Skill.rune_3),
    'bull_rush': (Barbarian._furious_charge, Skill.rune_4),
    'dreadnought': (Barbarian._furious_charge, Skill.rune_5),

    # overpower
    'overpower': (Barbarian._overpower, Skill.rune_0),
    'storm_of_steel': (Barbarian._overpower, Skill.rune_1),
    'killing_spree': (Barbarian._overpower, Skill.rune_2),
    'crushing_advance': (Barbarian._overpower, Skill.rune_3),
    'momentum': (Barbarian._overpower, Skill.rune_4),
    'revel': (Barbarian._overpower, Skill.rune_5),

    # weapon_throw
    'weapon_throw': (Barbarian._weapon_throw, Skill.rune_0),
    'mighty_throw': (Barbarian._weapon_throw, Skill.rune_1),
    'ricochet': (Barbarian._weapon_throw, Skill.rune_2),
    'throwing_hammer': (Barbarian._weapon_throw, Skill.rune_3),
    'stupefy': (Barbarian._weapon_throw, Skill.rune_4),
    'dread_bomb': (Barbarian._weapon_throw, Skill.rune_5),

    # threatening_shout
    'threatening_shout': (Barbarian._threatening_shout, Skill.rune_0),
    'intimidate': (Barbarian._threatening_shout, Skill.rune_1),
    'falter': (Barbarian._threatening_shout, Skill.rune_2),
    'grim_harvest': (Barbarian._threatening_shout, Skill.rune_3),
    'demoralize': (Barbarian._threatening_shout, Skill.rune_4),
    'terrify': (Barbarian._threatening_shout, Skill.rune_5),

    # battle_rage
    'battle_rage': (Barbarian._battle_rage, Skill.rune_0),
    'marauders_rage': (Barbarian._battle_rage, Skill.rune_1),
    'ferocity': (Barbarian._battle_rage, Skill.rune_2),
    'swords_to_ploughshares': (Barbarian._battle_rage, Skill.rune_3),
    'into_the_fray': (Barbarian._battle_rage, Skill.rune_4),
    'bloodshed': (Barbarian._battle_rage, Skill.rune_5),

    # war_cry
    'war_cry': (Barbarian._war_cry, Skill.rune_0),
    'hardened_wrath': (Barbarian._war_cry, Skill.rune_1),
    'charge!': (Barbarian._war_cry, Skill.rune_2),
    'invigorate': (Barbarian._war_cry, Skill.rune_3),
    'veterans_warning': (Barbarian._war_cry, Skill.rune_4),
    'impunity': (Barbarian._war_cry, Skill.rune_5),

    # earthquake
    'earthquake': (Barbarian._earthquake, Skill.rune_0),
    'giants_stride': (Barbarian._earthquake, Skill.rune_1),
    'chilling_earth': (Barbarian._earthquake, Skill.rune_2),
    'the_mountains_call': (Barbarian._earthquake, Skill.rune_3),
    'aftershocks': (Barbarian._earthquake, Skill.rune_4),
    'path_of_fire': (Barbarian._earthquake, Skill.rune_5),

    # call_of_the_ancients
    'call_of_the_ancients': (Barbarian._call_of_the_ancients, Skill.rune_0),
    'the_council_rises': (Barbarian._call_of_the_ancients, Skill.rune_1),
    'duty_to_the_clan': (Barbarian._call_of_the_ancients, Skill.rune_2),
    'korlics_might': (Barbarian._call_of_the_ancients, Skill.rune_3),
    'madawcs_madness': (Barbarian._call_of_the_ancients, Skill.rune_4),
    'talics_anger': (Barbarian._call_of_the_ancients, Skill.rune_5),

    # wrath_of_the_berserker
    'wrath_of_the_berserker': (Barbarian._wrath_of_the_berserker, Skill.rune_0),
    'arreats_wail': (Barbarian._wrath_of_the_berserker, Skill.rune_1),
    'insanity': (Barbarian._wrath_of_the_berserker, Skill.rune_2),
    'slaughter': (Barbarian._wrath_of_the_berserker, Skill.rune_3),
    'striding_giant': (Barbarian._wrath_of_the_berserker, Skill.rune_4),
    'thrive_on_chaos': (Barbarian._wrath_of_the_berserker, Skill.rune_5),

    # Passives
    'pound_of_flesh': Skill.passive_0_0,
    'ruthless': Skill.passive_0_1,
    'nerves_of_steel': Skill.passive_0_2,
    'weapons_master': Skill.passive_0_3,
    'berserker_rage': Skill.passive_1_0,
    'inspiring_presence': Skill.passive_1_1,
    'bloodthirst': Skill.passive_1_2,
    'animosity': Skill.passive_1_3,
    'superstition': Skill.passive_2_0,
    'tough_as_nails': Skill.passive_2_1,
    'no_escape': Skill.passive_2_2,
    'relentless': Skill.passive_2_3,
    'brawler': Skill.passive_3_4_0,
    'juggernaut': Skill.passive_3_4_1,
    'unforgiving': Skill.passive_3_4_2,
    'boon_of_bulkathos': Skill.passive_3_4_3,

})



class WitchDoctor:
    # Skills
    _poison_dart = Pages.page_0, Skill.ability_4_0
    _corpse_spiders = Pages.page_0, Skill.ability_4_1
    _plague_of_toads = Pages.page_0, Skill.ability_4_2
    _firebomb = Pages.page_0, Skill.ability_4_3
    _grasp_of_the_dead = Pages.page_1, Skill.ability_4_0
    _firebats = Pages.page_1, Skill.ability_4_1
    _haunt = Pages.page_1, Skill.ability_4_2
    _locust_swarm = Pages.page_1, Skill.ability_4_3
    _summon_zombie_dogs = Pages.page_2, Skill.ability_4_0
    _horrify = Pages.page_2, Skill.ability_4_1
    _spirit_walk = Pages.page_2, Skill.ability_4_2
    _hex = Pages.page_2, Skill.ability_4_3
    _soul_harvest = Pages.page_3, Skill.ability_3_0
    _sacrifice = Pages.page_3, Skill.ability_3_1
    _mass_confusion = Pages.page_3, Skill.ability_3_2
    _zombie_charger = Pages.page_4, Skill.ability_4_0
    _spirit_barrage = Pages.page_4, Skill.ability_4_1
    _acid_cloud = Pages.page_4, Skill.ability_4_2
    _wall_of_zombies = Pages.page_4, Skill.ability_4_3
    _gargantuan = Pages.page_5, Skill.ability_3_0
    _big_bad_voodoo = Pages.page_5, Skill.ability_3_1
    _fetish_army = Pages.page_5, Skill.ability_3_2

witch_doctor = attrdict({
    # poison dart
    'poison_dart': (WitchDoctor._poison_dart, Skill.rune_0),
    'splinters': (WitchDoctor._poison_dart, Skill.rune_1),
    'numbing_dart': (WitchDoctor._poison_dart, Skill.rune_2),
    'spined_dart': (WitchDoctor._poison_dart, Skill.rune_3),
    'flaming_dart': (WitchDoctor._poison_dart, Skill.rune_4),
    'snake_to_the_face': (WitchDoctor._poison_dart, Skill.rune_5),
    # Corpse spiders
    'corpse_spiders': (WitchDoctor._corpse_spiders, Skill.rune_0),
    'leaping_spiders': (WitchDoctor._corpse_spiders, Skill.rune_1),
    'spider_queen': (WitchDoctor._corpse_spiders, Skill.rune_2),
    'widowmakers': (WitchDoctor._corpse_spiders, Skill.rune_3),
    'medusa_spiders': (WitchDoctor._corpse_spiders, Skill.rune_4),
    'blazing_spiders': (WitchDoctor._corpse_spiders, Skill.rune_5),
    # Plague of toads
    'plague_of_toads': (WitchDoctor._plague_of_toads, Skill.rune_0),
    'explosive_toads': (WitchDoctor._plague_of_toads, Skill.rune_1),
    'toad_of_hugeness': (WitchDoctor._plague_of_toads, Skill.rune_2),
    'rain_of_toads': (WitchDoctor._plague_of_toads, Skill.rune_3),
    'addling_toads': (WitchDoctor._plague_of_toads, Skill.rune_4),
    'toad_affinity': (WitchDoctor._plague_of_toads, Skill.rune_5),
    # Firebomb
    'firebomb': (WitchDoctor._firebomb, Skill.rune_0),
    'flash_fire': (WitchDoctor._firebomb, Skill.rune_1),
    'roll_the_bones': (WitchDoctor._firebomb, Skill.rune_2),
    'fire_pit': (WitchDoctor._firebomb, Skill.rune_3),
    'pyrogeist': (WitchDoctor._firebomb, Skill.rune_4),
    'ghost_bomb': (WitchDoctor._firebomb, Skill.rune_5),
    # Grasp of the dead
    'grasp_of_the_dead': (WitchDoctor._grasp_of_the_dead, Skill.rune_0),
    'unbreakable_grasp': (WitchDoctor._grasp_of_the_dead, Skill.rune_1),
    'groping_eels': (WitchDoctor._grasp_of_the_dead, Skill.rune_2),
    'death_is_life': (WitchDoctor._grasp_of_the_dead, Skill.rune_3),
    'desperate_grasp': (WitchDoctor._grasp_of_the_dead, Skill.rune_4),
    'rain_of_corpses': (WitchDoctor._grasp_of_the_dead, Skill.rune_5),
    # firebats
    'firebats': (WitchDoctor._firebats, Skill.rune_0),
    'dire_bats': (WitchDoctor._firebats, Skill.rune_1),
    'vampire_bats': (WitchDoctor._firebats, Skill.rune_2),
    'plague_bats': (WitchDoctor._firebats, Skill.rune_3),
    'hungry_bats': (WitchDoctor._firebats, Skill.rune_4),
    'cloud_of_bats': (WitchDoctor._firebats, Skill.rune_5),
    # haunt
    'haunt': (WitchDoctor._haunt, Skill.rune_0),
    'consuming_spirit': (WitchDoctor._haunt, Skill.rune_1),
    'resentful_spirit': (WitchDoctor._haunt, Skill.rune_2),
    'lingering_spirit': (WitchDoctor._haunt, Skill.rune_3),
    'grasping_spirit': (WitchDoctor._haunt, Skill.rune_4),
    'draining_spirit': (WitchDoctor._haunt, Skill.rune_5),
    # locust swarm
    'locust_swarm': (WitchDoctor._locust_swarm, Skill.rune_0),
    'pestilence': (WitchDoctor._locust_swarm, Skill.rune_1),
    'devouring_swarm': (WitchDoctor._locust_swarm, Skill.rune_2),
    'cloud_of_insects': (WitchDoctor._locust_swarm, Skill.rune_3),
    'diseased_swarm': (WitchDoctor._locust_swarm, Skill.rune_4),
    'searing_locusts': (WitchDoctor._locust_swarm, Skill.rune_5),
    # summon zombie dogs
    'summon_zombie_dogs': (WitchDoctor._summon_zombie_dogs, Skill.rune_0),
    'rabid_dogs': (WitchDoctor._summon_zombie_dogs, Skill.rune_1),
    'final_gift': (WitchDoctor._summon_zombie_dogs, Skill.rune_2),
    'life_link': (WitchDoctor._summon_zombie_dogs, Skill.rune_3),
    'burning_dogs': (WitchDoctor._summon_zombie_dogs, Skill.rune_4),
    'leeching_beasts': (WitchDoctor._summon_zombie_dogs, Skill.rune_5),
    # horrify
    'horrify': (WitchDoctor._horrify, Skill.rune_0),
    'phobia': (WitchDoctor._horrify, Skill.rune_1),
    'stalker': (WitchDoctor._horrify, Skill.rune_2),
    'face_of_death': (WitchDoctor._horrify, Skill.rune_3),
    'frightening_aspect': (WitchDoctor._horrify, Skill.rune_4),
    'ruthless_terror': (WitchDoctor._horrify, Skill.rune_5),
    # spirit walk
    'spirit_walk': (WitchDoctor._spirit_walk, Skill.rune_0),
    'jaunt': (WitchDoctor._spirit_walk, Skill.rune_1),
    'honored_guest': (WitchDoctor._spirit_walk, Skill.rune_2),
    'umbral_shock': (WitchDoctor._spirit_walk, Skill.rune_3),
    'severance': (WitchDoctor._spirit_walk, Skill.rune_4),
    'healing_journey': (WitchDoctor._spirit_walk, Skill.rune_5),
    # hex
    'hex': (WitchDoctor._hex, Skill.rune_0),
    'hedge_magic': (WitchDoctor._hex, Skill.rune_1),
    'jinx': (WitchDoctor._hex, Skill.rune_2),
    'angry_chicken': (WitchDoctor._hex, Skill.rune_3),
    'painful_transformation': (WitchDoctor._hex, Skill.rune_4),
    'unstable_form': (WitchDoctor._hex, Skill.rune_5),
    # soul harvest
    'soul_harvest': (WitchDoctor._soul_harvest, Skill.rune_0),
    'swallow_your_soul': (WitchDoctor._soul_harvest, Skill.rune_1),
    'siphon': (WitchDoctor._soul_harvest, Skill.rune_2),
    'languish': (WitchDoctor._soul_harvest, Skill.rune_3),
    'soul_to_waste': (WitchDoctor._soul_harvest, Skill.rune_4),
    'vengeful_spirit': (WitchDoctor._soul_harvest, Skill.rune_5),
    # sacrifice
    'sacrifice': (WitchDoctor._sacrifice, Skill.rune_0),
    'black_blood': (WitchDoctor._sacrifice, Skill.rune_1),
    'next_of_kin': (WitchDoctor._sacrifice, Skill.rune_2),
    'pride': (WitchDoctor._sacrifice, Skill.rune_3),
    'for_the_master': (WitchDoctor._sacrifice, Skill.rune_4),
    'provoke_the_pack': (WitchDoctor._sacrifice, Skill.rune_5),
    # mass confusion
    'mass_confusion': (WitchDoctor._mass_confusion, Skill.rune_0),
    'unstable_realm': (WitchDoctor._mass_confusion, Skill.rune_1),
    'devolution': (WitchDoctor._mass_confusion, Skill.rune_2),
    'mass_hysteria': (WitchDoctor._mass_confusion, Skill.rune_3),
    'paranoia': (WitchDoctor._mass_confusion, Skill.rune_4),
    'mass_hallucination': (WitchDoctor._mass_confusion, Skill.rune_5),
    # zombie charger
    'zombie_charger': (WitchDoctor._zombie_charger, Skill.rune_0),
    'leperous_zombie': (WitchDoctor._zombie_charger, Skill.rune_1),
    'undeath': (WitchDoctor._zombie_charger, Skill.rune_2),
    'wave_of_zombies': (WitchDoctor._zombie_charger, Skill.rune_3),
    'explosive_beast': (WitchDoctor._zombie_charger, Skill.rune_4),
    'zombie_bears': (WitchDoctor._zombie_charger, Skill.rune_5),
    # spirit barrage
    'spirit_barrage': (WitchDoctor._spirit_barrage, Skill.rune_0),
    'the_spirit_is_willing': (WitchDoctor._spirit_barrage, Skill.rune_1),
    'well_of_souls': (WitchDoctor._spirit_barrage, Skill.rune_2),
    'phantasm': (WitchDoctor._spirit_barrage, Skill.rune_3),
    'phlebotomize': (WitchDoctor._spirit_barrage, Skill.rune_4),
    'manitou': (WitchDoctor._spirit_barrage, Skill.rune_5),
    # acid cloud
    'acid_cloud': (WitchDoctor._acid_cloud, Skill.rune_0),
    'acid_rain': (WitchDoctor._acid_cloud, Skill.rune_1),
    'lob_blob_bomb': (WitchDoctor._acid_cloud, Skill.rune_2),
    'slow_burn': (WitchDoctor._acid_cloud, Skill.rune_3),
    'kiss_of_death': (WitchDoctor._acid_cloud, Skill.rune_4),
    'corpse_bomb': (WitchDoctor._acid_cloud, Skill.rune_5),
    # wall of zombies
    'wall_of_zombies': (WitchDoctor._wall_of_zombies, Skill.rune_0),
    'barricade': (WitchDoctor._wall_of_zombies, Skill.rune_1),
    'unrelenting_grip': (WitchDoctor._wall_of_zombies, Skill.rune_2),
    'creepers': (WitchDoctor._wall_of_zombies, Skill.rune_3),
    'pile_on': (WitchDoctor._wall_of_zombies, Skill.rune_4),
    'dead_rush': (WitchDoctor._wall_of_zombies, Skill.rune_5),
    # gargantuan
    'gargantuan': (WitchDoctor._gargantuan, Skill.rune_0),
    'humongoid': (WitchDoctor._gargantuan, Skill.rune_1),
    'restless_giant': (WitchDoctor._gargantuan, Skill.rune_2),
    'wrathful_protector': (WitchDoctor._gargantuan, Skill.rune_3),
    'big_stinker': (WitchDoctor._gargantuan, Skill.rune_4),
    'bruiser': (WitchDoctor._gargantuan, Skill.rune_5),
    # big bad voodoo
    'big_bad_voodoo': (WitchDoctor._big_bad_voodoo, Skill.rune_0),
    'jungle_drums': (WitchDoctor._big_bad_voodoo, Skill.rune_1),
    'rain_dance': (WitchDoctor._big_bad_voodoo, Skill.rune_2),
    'slam_dance': (WitchDoctor._big_bad_voodoo, Skill.rune_3),
    'ghost_trance': (WitchDoctor._big_bad_voodoo, Skill.rune_4),
    'boogie_man': (WitchDoctor._big_bad_voodoo, Skill.rune_5),
    # fetish army
    'fetish_army': (WitchDoctor._fetish_army, Skill.rune_0),
    'fetish_ambush': (WitchDoctor._fetish_army, Skill.rune_1),
    'devoted_following': (WitchDoctor._fetish_army, Skill.rune_2),
    'legion_of_daggers': (WitchDoctor._fetish_army, Skill.rune_3),
    'tiki_torchers': (WitchDoctor._fetish_army, Skill.rune_4),
    'head_hunters': (WitchDoctor._fetish_army, Skill.rune_5),

    # Passives
    'circle_of_life': Skill.passive_0_0,
    'jungle_fortitude': Skill.passive_0_1,
    'spiritual_attunement': Skill.passive_0_2,
    'gruesome_feast': Skill.passive_0_3,
    'bad_medicine': Skill.passive_1_0,
    'blood_ritual': Skill.passive_1_1,
    'zombie_handler': Skill.passive_1_2,
    'pierce_the_veil': Skill.passive_1_3,
    'fetish_sycophants': Skill.passive_2_0,
    'spirit_vessel': Skill.passive_2_1,
    'rush_of_essence': Skill.passive_2_2,
    'vision_quest': Skill.passive_2_3,
    'fierce_loyalty': Skill.passive_3_3_0,
    'grave_injustice': Skill.passive_3_3_1,
    'tribal_rites': Skill.passive_3_3_2,
})


KNOWN_ABILITIES = witch_doctor.keys() + barbarian.keys()
ABILITY_ASSOC = { }

for _class in (witch_doctor, barbarian):
    ABILITY_ASSOC.update(_class)
