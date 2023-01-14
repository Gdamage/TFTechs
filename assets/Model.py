# changes hierachy level to import other modules
from sys import path
path.insert(1, '.')

# module imports
from json import load

# local imports
from utils import resource_path, string_starts_with

class AbilityVariable:
    def __init__(
        self, 
        name, 
        value):
        self.name = name
        self.value = value
class Ability:
    def __init__(
        self,
        description,
        icon,
        name,
        variables):
        self.description = description
        self.icon = icon
        self.name = name
        self.variables = variables
class ChampionStats:
    def __init__(
        self,
        armor,
        attack_speed,
        crit_chance,
        crit_multiplier,
        attack_damage,
        hp,
        initial_mana,
        magic_resist,
        mana,
        attack_range):
        self.armor = armor
        self.attack_speed = attack_speed
        self.crit_chance = crit_chance
        self.crit_multiplier = crit_multiplier
        self.attack_damage = attack_damage
        self.hp = hp
        self.initial_mana = initial_mana
        self.magic_resist = magic_resist
        self.mana = mana
        self.attack_range = attack_range
class Champion:
    """Champion attributes"""
    def __init__(
        self,
        name,
        champion_id,
        cost,
        ability,
        icon,
        traits,
        stats):
        self.name = name
        self.champion_id = champion_id
        self.cost = cost
        self.ability = ability
        self.icon = icon
        self.traits = traits
        self.stats = stats
        
    def print_attributes(self):
        print(f'id: {self.id}')
        print(f'name {self.name}')
        print(f'cost: {self.cost}')
class Trait:
    def __init__(
        self,
        trait_id,
        description,
        icon,
        name,
        effects):
        self.trait_id = trait_id
        self.description = description
        self.icon = icon
        self.name = name
        self.effects = effects
class TraitEffects:
    def __init__(
        self,
        min_units,
        max_units,
        style,
        variables):
        self.min_units = min_units
        self.max_units = max_units
        self.style = style
        self.variables = variables

class Model:
    def __init__(self):
        self.lang = 'en_US'
        self.set_number = '8'
        self.api_prefix = f'TFT{self.set_number}'

        try:
            lang_file_path = resource_path(f'lang/{self.lang}.json')
            
            # opens selected language file
            with open(lang_file_path, 'r') as lf: 
                lang_file = load(lf)
                
                # items
                self.items = lang_file['items']
                for item in self.items:
                    item_prefix = f'{self.api_prefix}_Item'
                    augment_prefix = f'{self.api_prefix}_Augment'
                    admin_cause_prefix = f'{self.api_prefix}_AdminCause'
                    admin_effect_prefix = f'{self.api_prefix}_AdminEffect'
                    hyper_roll_augment_prefix = f'{self.api_prefix}_HyperRollAugment'
                    consumable_prefix = f'{self.api_prefix}_Consumable'
                    if(string_starts_with(item['apiName'], self.api_prefix)):
                        # set items
                        if(string_starts_with(item['apiName'], item_prefix)):
                            None
                        # augments
                        elif(string_starts_with(item['apiName'], augment_prefix)):
                            None
                        # admin cause
                        elif(string_starts_with(item['apiName'], admin_cause_prefix)):
                            None
                        # admin effect
                        elif(string_starts_with(item['apiName'], admin_effect_prefix)):
                            None
                        # hyper roll augments
                        elif(string_starts_with(item['apiName'], hyper_roll_augment_prefix)):
                            None
                        # consumables
                        elif(string_starts_with(item['apiName'], consumable_prefix)):
                            None
                        else:
                            print(item['apiName'])

                # set data
                self.set_data = lang_file['setData']

                # sets
                sets = lang_file['sets']
                self.current_set = sets[self.set_number]
                self.set_name = self.current_set['name']

                # set champions
                self.champion_list = []
                for champion in self.current_set['champions']:
                    # checks for 'TFT{set_number} substring on the id
                    substring = f'TFT{self.set_number}'
                    champion_id = champion['apiName']
                    
                    # if champion belongs to current set
                    if(string_starts_with(champion_id, substring)):
                        # ability variables
                        variable_list = []
                        for variable in champion['ability']['variables']:
                            variable_list.append(
                                AbilityVariable(
                                    name = variable['name'], 
                                    value = variable['value']))
                        
                        # ability attributes
                        champ_ability = Ability(
                            description = champion['ability']['desc'], 
                            icon = champion['ability']['icon'], 
                            name = champion['ability']['name'],
                            variables = variable_list)

                        # champion stats
                        champion_stats = ChampionStats(
                            armor = champion['stats']['armor'],
                            attack_speed = champion['stats']['attackSpeed'],
                            crit_chance = champion['stats']['critChance'],
                            crit_multiplier = champion['stats']['critMultiplier'],
                            attack_damage = champion['stats']['damage'],
                            hp = champion['stats']['hp'],
                            initial_mana = champion['stats']['initialMana'],
                            magic_resist = champion['stats']['magicResist'],
                            mana = champion['stats']['mana'],
                            attack_range = champion['stats']['range'])
                        
                        # adds champion to champion list
                        self.champion_list.append(
                            Champion(
                                name = champion['name'],
                                champion_id = champion['apiName'],
                                cost = champion['cost'],
                                ability = champ_ability,
                                icon = champion['icon'],
                                traits = champion['traits'],
                                stats = champion_stats))
                    
                # set traits
                self.trait_list = []
                for trait in self.current_set['traits']: 
                    # trait effects
                    effect_list = []
                    for effect in trait['effects']:
                        # effect variables
                        variable_list = []
                        for variable in effect['variables']:
                            value = effect['variables'][variable]
                            variable_list.append(AbilityVariable(
                                name = variable, 
                                value = value))
                        effect_list.append(
                            TraitEffects(
                                min_units = effect['minUnits'],
                                max_units = effect['maxUnits'],
                                style = effect['style'],
                                variables = variable_list))
                    self.trait_list.append(Trait(
                        trait_id = trait['apiName'],
                        description = trait['desc'],
                        icon = trait['icon'],
                        name = trait['name'],
                        effects = effect_list))
        except IOError:
            print('erro ao abrir arquivo')

test = Model()
# eof