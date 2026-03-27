# Minecraft Gladiator

> Význam jména - *Gladiátor* - profesionální bojovník, který za účelem pobavení publika zápasil v arénách s jinými gladiátory nebo divokými zvířaty.

## Odborný článek

Gladiator je místo pro optimalizaci vašeho bojového stylu v minecraftu. Jejím účelem je postupný trénink mechanik, kategorizace taktik podle typu souboje (např. PotPvP, Mace, Uhc, Smp).

### Funkce

#### Sdílení nastavení
Uživatel může vygenerovat konfigurační profil, pomocí kterého může sdílet své nastavení (keybindy, sensitivita myši, crosshair design) se všemi uživateli. Stačí jen jít do své .minecraft složky, najít options.txt a vložit celá svá nastavení, poté jen manuálně napsat jaké itemy používáte v každém hotbar slotu.

#### Řazení taktik
Uživatelé budou moct nahrát různé taktiky (např. stun slam, shield drain, atd.). Poté je můžou uživatelé ohodnotit pětihvězdičkovým systémem. Samotné strategie budou poté řazeny do kategorií, do kterých patří.
Nahrávky videí obsahujících taktiky budou ve formě odkazu. (např. youtube, medal.tv, atd.)

### Role

#### Začátečník (Noob)
Nováček nemá přístup k pokročilým analytickým grafům. Zaměřuje se na základní techniky pohybu a fixaci inventáře.

#### Pokročilý (Intermediate)
Soutěžící využívá pokročilou analytiku pro ladění svého stylu. Je schopen definovat vlastní tréninkové rutiny a spravovat konfigurace, které jsou uloženy na lokální bázi.

#### Profík (Pro)
Účet Taktika je určen pro lídry klanů. Může spravovat sdílené taktické dokumenty pro celý tým, definovat globální pravidla pro "hotbar" layouty a provádět týmové přehledy.

## ER-D

![IMG_20260327_010223](https://github.com/user-attachments/assets/3118b9c6-4b35-46ea-986f-583a158dd7da)


## Nastavení a Konfigurace



```bash
# Názorná ukázka sdílení nastavení:



Kategorie = mace
slot_1 = breach mace
slot_2 = wind charge
slot_3 =  density mace
slot_4 = golden apple
slot_5 = shield
slot_6 = elytra
slot_7 = ender pearl
slot_8 = sword
slot_9 = axe
offhand = totem of undying



option.txt

version:4671
ao:true
biomeBlendRadius:3
chunkSectionFadeInTime:0.75
cutoutLeaves:true
enableVsync:false
entityDistanceScaling:5.0
entityShadows:false
forceUnicodeFont:false
japaneseGlyphVariants:false
fov:1.0
fovEffectScale:0.0
darknessEffectScale:0.0
glintSpeed:0.5
glintStrength:0.75
graphicsPreset:"custom"
prioritizeChunkUpdates:2
fullscreen:true
gamma:0.5
guiScale:2
maxAnisotropyBit:2
textureFiltering:0
maxFps:260
improvedTransparency:false
inactivityFpsLimit:"afk"
mipmapLevels:4
narrator:0
particles:2
reducedDebugInfo:false
renderClouds:"false"
cloudRange:2
renderDistance:10
simulationDistance:5
screenEffectScale:0.0
soundDevice:""
vignette:true
weatherRadius:3
autoJump:false
rotateWithMinecart:false
operatorItemsTab:false
autoSuggestions:true
chatColors:true
chatLinks:true
chatLinksPrompt:true
discrete_mouse_scroll:false
invertXMouse:false
invertYMouse:false
realmsNotifications:true
showSubtitles:false
directionalAudio:false
touchscreen:false
bobView:false
toggleCrouch:false
toggleSprint:false
toggleAttack:false
toggleUse:false
sprintWindow:7
darkMojangStudiosBackground:false
hideLightningFlashes:false
hideSplashTexts:false
mouseSensitivity:0.5140845070422535
damageTiltStrength:0.0
highContrast:false
highContrastBlockOutline:false
narratorHotkey:true
resourcePacks:["vanilla","file/ATG12\u0027s Overlay.zip"]
incompatibleResourcePacks:[]
lastServer:nX2AR.verify.mctiers.com
lang:en_us
chatVisibility:0
chatOpacity:1.0
chatLineSpacing:0.0
textBackgroundOpacity:0.5
backgroundForChatOnly:true
hideServerAddress:false
advancedItemTooltips:true
pauseOnLostFocus:true
overrideWidth:0
overrideHeight:0
chatHeightFocused:1.0
chatDelay:0.0
chatHeightUnfocused:0.4375
chatScale:1.0
chatWidth:1.0
notificationDisplayTime:1.0
useNativeTransport:true
mainHand:"right"
attackIndicator:1
tutorialStep:none
mouseWheelSensitivity:1.0
rawMouseInput:true
allowCursorChanges:true
glDebugVerbosity:1
skipMultiplayerWarning:true
hideMatchedNames:true
joinedFirstServer:true
syncChunkWrites:true
showAutosaveIndicator:true
allowServerListing:true
onlyShowSecureChat:false
saveChatDrafts:false
panoramaScrollSpeed:1.0
telemetryOptInExtra:false
onboardAccessibility:false
menuBackgroundBlurriness:5
startedCleanly:true
musicToast:"never"
musicFrequency:"DEFAULT"
key_key.attack:key.mouse.left
key_key.use:key.mouse.right
key_key.forward:key.keyboard.w
key_key.left:key.keyboard.a
key_key.back:key.keyboard.s
key_key.right:key.keyboard.d
key_key.jump:key.keyboard.space
key_key.sneak:key.keyboard.left.shift
key_key.sprint:key.keyboard.page.up
key_key.drop:key.keyboard.caps.lock
key_key.inventory:key.keyboard.e
key_key.chat:key.keyboard.t
key_key.playerlist:key.keyboard.grave.accent
key_key.pickItem:key.mouse.middle
key_key.command:key.keyboard.slash
key_key.socialInteractions:key.keyboard.p
key_key.toggleGui:key.keyboard.f1
key_key.toggleSpectatorShaderEffects:key.keyboard.f4
key_key.screenshot:key.keyboard.f2
key_key.togglePerspective:key.keyboard.x
key_key.smoothCamera:key.keyboard.unknown
key_key.fullscreen:key.keyboard.f11
key_key.spectatorOutlines:key.keyboard.unknown
key_key.spectatorHotbar:key.mouse.middle
key_key.swapOffhand:key.keyboard.2
key_key.saveToolbarActivator:key.keyboard.unknown
key_key.loadToolbarActivator:key.keyboard.unknown
key_key.advancements:key.keyboard.unknown
key_key.quickActions:key.keyboard.g
key_key.debug.overlay:key.keyboard.f3
key_key.debug.modifier:key.keyboard.f3
key_key.hotbar.1:key.keyboard.1
key_key.hotbar.2:key.mouse.4
key_key.hotbar.3:key.keyboard.3
key_key.hotbar.4:key.keyboard.4
key_key.hotbar.5:key.keyboard.f
key_key.hotbar.6:key.keyboard.tab
key_key.hotbar.7:key.mouse.5
key_key.hotbar.8:key.keyboard.r
key_key.hotbar.9:key.keyboard.q
key_key.debug.reloadChunk:key.keyboard.a
key_key.debug.showHitboxes:key.keyboard.b
key_key.debug.clearChat:key.keyboard.d
key_key.debug.crash:key.keyboard.unknown
key_key.debug.showChunkBorders:key.keyboard.g
key_key.debug.showAdvancedTooltips:key.keyboard.h
key_key.debug.copyRecreateCommand:key.keyboard.i
key_key.debug.spectate:key.keyboard.n
key_key.debug.switchGameMode:key.keyboard.f4
key_key.debug.debugOptions:key.keyboard.f6
key_key.debug.focusPause:key.keyboard.p
key_key.debug.dumpDynamicTextures:key.keyboard.s
key_key.debug.reloadResourcePacks:key.keyboard.t
key_key.debug.profiling:key.keyboard.l
key_key.debug.copyLocation:key.keyboard.c
key_key.debug.dumpVersion:key.keyboard.v
key_key.debug.profilingChart:key.keyboard.1
key_key.debug.fpsCharts:key.keyboard.2
key_key.debug.networkCharts:key.keyboard.3
key_key.push_to_talk:key.keyboard.keypad.1
key_key.whisper:key.keyboard.keypad.7
key_key.mute_microphone:key.keyboard.keypad.multiply
key_key.disable_voice_chat:key.keyboard.keypad.2
key_key.hide_icons:key.keyboard.h
key_key.voice_chat:key.keyboard.n
key_key.voice_chat_settings:key.keyboard.unknown
key_key.voice_chat_group:key.keyboard.unknown
key_key.voice_chat_toggle_recording:key.keyboard.unknown
key_key.voice_chat_adjust_volumes:key.keyboard.unknown
key_gui.xaero_open_map:key.keyboard.keypad.5
key_gui.xaero_open_settings:key.keyboard.keypad.6
key_gui.xaero_world_map_server_settings:key.keyboard.unknown
key_gui.xaero_map_zoom_in:key.keyboard.unknown
key_gui.xaero_map_zoom_out:key.keyboard.unknown
key_gui.xaero_quick_confirm:key.keyboard.right.shift
key_gui.xaero_toggle_dimension:key.keyboard.unknown
key_gui.xaero_toggle_tracked_players:key.keyboard.unknown
key_gui.xaero_toggle_pac_chunk_claims:key.keyboard.unknown
key_Mod Menu:key.keyboard.right.shift
key_Waypoint Menu:key.keyboard.left
key_Create Waypoint:key.keyboard.unknown
key_Emote Wheel:key.keyboard.unknown
key_Spray Wheel:key.keyboard.y
key_Spray Snap Keybind:key.keyboard.unknown
key_Sprint Keybind:key.keyboard.keypad.enter
key_Sneak Keybind:key.keyboard.keypad.1
key_Zoom Key:key.keyboard.c
key_Toggle Display of Waypoints:key.keyboard.keypad.divide
key_Toggle Chat Visibility:key.keyboard.unknown
key_Reset Counts Keybind:key.keyboard.unknown
key_Freelook:key.keyboard.left.alt
key_Third Person Key:key.keyboard.left.alt
key_Forward View Key:key.keyboard.unknown
key_Skip Node:key.keyboard.g
key_Send Coordinates Keybind:key.keyboard.unknown
soundCategory_master:0.2963576018810272
soundCategory_music:0.0
soundCategory_record:0.22183097898960114
soundCategory_weather:0.0
soundCategory_block:0.23591549694538116
soundCategory_hostile:0.44718310236930847
soundCategory_neutral:0.0
soundCategory_player:1.0
soundCategory_ambient:0.23943662643432617
soundCategory_voice:0.0
soundCategory_ui:1.0
modelPart_cape:true
modelPart_jacket:true
modelPart_left_sleeve:true
modelPart_right_sleeve:true
modelPart_left_pants_leg:true
modelPart_right_pants_leg:true
modelPart_hat:true
