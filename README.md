# Minecraft Gladiator

> Význam jména - *Gladiátor* - profesionální bojovník, který za účelem pobavení publika zápasil v arénách s jinými gladiátory nebo divokými zvířaty.

## Odborný článek

Gladiator je místo pro optimalizaci vašeho bojového stylu v minecraftu. Jejím účelem je postupný trénink mechanik, kategorizace taktik podle typu souboje (např. PotPvP, Mace, Uhc, Smp).

### Funkce

#### Sdílení nastavení
Uživatel může vygenerovat konfigurační profil, pomocí kterého může sdílet své nastavení (keybindy, sensitivita myši, crosshair design) se všemi uživateli. Stačí jen jít do své .minecraft složky, najít options.txt a vložit celá svá nastavení, poté jen manuálně napsat jaké itemy používáte v každém hotbar slotu.

#### Řazení taktik
Uživatelé budou moct nahrát různé taktiky (např. stun slam, shield drain, atd.). Poté je můžou uživatelé ohodnotit pětihvězdičkovým systémem. Samotné strategie budou poté řazeny do kategorií, do kterých patří.

### Role

#### Začátečník (Noob)
Nováček nemá přístup k pokročilým analytickým grafům. Zaměřuje se na základní techniky pohybu a fixaci inventáře.

#### Pokročilý (Intermediate)
Soutěžící využívá pokročilou analytiku pro ladění svého stylu. Je schopen definovat vlastní tréninkové rutiny a spravovat konfigurace, které jsou uloženy na lokální bázi.

#### Profík (Pro)
Účet Taktika je určen pro lídry klanů. Může spravovat sdílené taktické dokumenty pro celý tým, definovat globální pravidla pro "hotbar" layouty a provádět týmové přehledy.

## Nastavení a Konfigurace

Gladiator je koncipován jako soubor standardizovaných profilů pro rychlou aplikaci.

### CLI (Command Line Interface)

```bash
# Aplikace standardizovaného PvP profilu
gladiator apply --profile competitive --fov 90
gladiator verify --integrity --check-mouse-accel
Konfigurace prostředí
<details>
<summary><b>config.json (Standardizovaný layout)</b></summary>

JSON
{
  "pvp_settings": {
    "fov": 90,
    "sensitivity": 45,
    "dynamic_fov": false,
    "hotbar_layout": [
      "sword",
      "rod",
      "gapple",
      "lava_bucket",
      "blocks",
      "water_bucket",
      "pearl",
      "blocks",
      "potion"
    ]
  }
}
</details>

<details>
<summary><b>keybinds.yml (Efektivní přístup)</b></summary>

YAML
keybinds:
  - action: "slot_1"
    key: "1"
  - action: "slot_2"
    key: "R"
  - action: "slot_3"
    key: "F"
  - action: "slot_4"
    key: "V"
  - action: "toggle_sprint"
    key: "CTRL"
