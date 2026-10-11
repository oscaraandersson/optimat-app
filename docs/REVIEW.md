# Granskning av nuvarande sida (v1)

Skriven innan omdesignen. Det här är vad som är svagt i `/workspace/optimat-app/` / https://oscaraandersson.github.io/optimat-app/.

## Innehåll som nu är fel
- **"Kommer snart"-pillret** är fel nu när appen finns i App Store, och det är en `<span>`, inte en länk.
- **"Soft launch · Sverige"** (överrubrik) är fel. Samma ord finns i `<title>`-liknande copy och i integritetssidans ingress ("vid soft launch").
- **Ingen App Store-länk** någonstans: ingen knapp, ingen länk i header, hero eller footer.
- **Rubriken** ("Planera maten från ditt skafferi — med makron och pris.") är lång och matchar inte taglinen "Recept efter pris och makron".
- **Titel/description** pratar om "recept- och skafferihanterare" och "lokal-först", internt språk som inte säljer. Saknar "ingen prenumeration".
- "kcal" och "Skafferi → recept"/"planera frukost, lunch, middag" lovar mer än appen behöver visa; "Sverige först" är en slogan, inte en funktion.

## Design
- **För många kort:** hero är ett kort, fyra fördelar är fyra kort, "Vad Optimat inte är" är ett kort, och integritetssidans text ligger i ytterligare kort. Allt har samma skugga och radie, så inget får hierarki. Oscar föredrar kortlöst (som i receptbilden).
- **Ingen produktbild alls.** Sidan visar inte hur appen ser ut. Inga skärmdumpar, ingen telefon.
- **Hierarkin är platt:** rubrik 36 px max, allt annat 15-17 px i grå text.
- **Smal layout (880 px)** på desktop med mycket tom yta och inget som drar blicken.
- Ingen tydlig primär handling (CTA).

## Teknik / SEO
- Google Fonts laddas från tredje part (integritet, och blockerar offline).
- Saknar Open Graph/Twitter-taggar, og:image, canonical, apple-touch-icon, favicon-fallback (bara SVG).
- Logotypen i header har ingen separat fokusstil; inga `:focus-visible`-stilar; ingen `prefers-reduced-motion`.
- Footern har tvåspråkiga länkar ("Hem / Home") som inte matchar resten av sidan.

## Plan för v2
Cardless: struktur via typografi, luft och hårlinjer. Hero med riktig skärmdump i telefonram, fyra funktionsrader (Skanna, Sortera, Bygg, Dela), en tyst text-remsa om integritet, en slut-CTA med enkel textknapp till App Store, och en footer med Instagram, Integritet och "vad Optimat inte är" som en mening. Självhostade typsnitt, full SEO. Max en behållare på hela sidan (slut-CTA:n).
