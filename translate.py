def rename_strings(text, replacements):
    for old_string, new_string in replacements.items():
        text = text.replace(old_string, new_string)
    return text

def process_file(filename, replacements):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        modified_content = rename_strings(content, replacements)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(modified_content)

if __name__ == "__main__":
    replacements = {
        "HPDelta": "Flat HP",
        "AttackDelta": "Flat ATK",
        "HPAddedRatio": "HP%",
        "AttackAddedRatio": "ATK%",
        "DefenceDelta": "Flat DEF",
        "DefenceAddedRatio": "DEF%",
        "CriticalChanceBase": "Crit Rate",
        "CriticalDamageBase": "Crit DMG",
        "HealRatioBase": "Outgoing Healing Bonus",
        "StatusProbabilityBase": "Effect Hit Rate",
        "SpeedDelta": "Speed",
        "PhysicalAddedRatio": "Physcial Damage",
        "FireAddedRatio": "Fire Damage",
        "IceAddedRatio": "Ice Damage",
        "ThunderAddedRatio": "Lightning Damage",
        "WindAddedRatio": "Wind Damage",
        "QuantumAddedRatio": "Quantum Damage",
        "ImaginaryAddedRatio": "Imaginary Damage",
        "BreakDamageAddedRatioBase": "Break Effect",
        "SPRatioBase": "Energy Regeneration",
        "StatusResistanceBase":"Effect Res"
    }

    input_files = [
        "RelicMainAffixConfig.json", 
        "RelicSubAffixConfig.json"
        ]

    for input_file in input_files:
        process_file(input_file, replacements)
        print(f"Processed {input_file}")
