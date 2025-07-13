# DATOS SIMULADOS DE EMPRENDIMIENTOS TURÍSTICOS EN LLOA
# Para agregar a través del admin de Django

emprendimientos_lloa = [
    {
        "title": "Café de Altura Pacchacamac",
        "subtitle": "Experiencia cafetera en los páramos",
        "description": "Descubre el proceso completo del café de altura en nuestra finca familiar ubicada a 3,200 metros sobre el nivel del mar. Ofrecemos tours guiados por los cultivos orgánicos, degustaciones de café recién tostado y talleres de preparación. Nuestro café, cultivado en los páramos de Lloa, destaca por su acidez equilibrada y notas florales únicas. Los visitantes pueden participar en la cosecha durante los meses de mayo a septiembre, aprender sobre el secado natural al sol y disfrutar de un desayuno tradicional con productos locales mientras contemplan las majestuosas vistas del Pichincha."
    },
    {
        "title": "Senderos Ancestrales Yanacocha",
        "subtitle": "Turismo comunitario y avistamiento de aves",
        "description": "Experimenta la riqueza natural de los bosques nublados de Lloa con nuestros guías nativos especializados en avistamiento de aves. Hemos registrado más de 180 especies de aves, incluyendo el emblemático cóndor andino, colibríes de páramo y tangaras multicolores. Nuestros senderos ecológicos te llevan por antiguos caminos indígenas utilizados por generaciones. Incluye caminatas de diferentes niveles de dificultad, desde paseos familiares de 2 horas hasta trekking de día completo. Ofrecemos hospedaje rural en cabañas ecológicas construidas con materiales locales y técnicas ancestrales de construcción."
    },
    {
        "title": "Granja Pedagógica Runa Wasí",
        "subtitle": "Aprendizaje rural y vida sostenible",
        "description": "Conecta con la vida rural tradicional en nuestra granja pedagógica familiar donde criamos llamas, alpacas, cuyes y gallinas criollas. Los visitantes participan en actividades cotidianas como el ordeño de vacas, recolección de huevos, alimentación de animales y elaboración de quesos artesanales. Ofrecemos talleres de hilado de lana de oveja, tejido en telar tradicional y preparación de platos típicos en horno de leña. Ideal para familias con niños, grupos escolares y personas interesadas en el turismo vivencial. Incluye almuerzos preparados con productos 100% orgánicos cultivados en nuestra propia huerta."
    },
    {
        "title": "Aventura Extrema Volcán Trek",
        "subtitle": "Adrenalina en las alturas del Pichincha",
        "description": "Vive la aventura más emocionante en las laderas del volcán Pichincha con nuestras actividades de turismo extremo. Ofrecemos escalada en roca en paredes naturales de hasta 40 metros, rappel en cascadas de montaña, mountain bike por senderos técnicos y parapente con vistas espectaculares a Quito y los valles circundantes. Nuestros guías certificados internacionalmente garantizan tu seguridad con equipos de primera calidad. Los paquetes incluyen desde experiencias de medio día para principiantes hasta expediciones de varios días para aventureros experimentados. También organizamos ascensiones nocturnas para observar las estrellas desde el refugio base a 4,200 metros de altura."
    },
    {
        "title": "Spa Termal Kushki Pakcha",
        "subtitle": "Relajación natural en aguas medicinales",
        "description": "Relájate en nuestras piscinas de aguas termales naturales ricas en minerales volcánicos, conocidas por sus propiedades curativas y relajantes. Ubicado en un entorno natural privilegiado rodeado de vegetación nativa, ofrecemos tratamientos de spa con plantas medicinales locales como eucalipto, romero y hierba luisa. Nuestros servicios incluyen masajes con piedras volcánicas calientes, baños de vapor con hierbas aromáticas, exfoliaciones corporales con arcilla volcánica y rituales de limpieza energética siguiendo tradiciones ancestrales. El complejo cuenta con áreas de descanso al aire libre, zona de meditación con vista panorámica y restaurante con gastronomía saludable preparada con ingredientes orgánicos locales."
    }
]

# INSTRUCCIONES PARA AGREGAR LOS DATOS:
# 1. Ir a http://127.0.0.1:8000/admin/
# 2. Hacer login con tu usuario administrador
# 3. Ir a la sección "Places" -> "Lugares"
# 4. Hacer clic en "Add lugar" para cada emprendimiento
# 5. Copiar y pegar los datos de título, subtítulo y descripción
# 6. Subir las imágenes correspondientes a cada emprendimiento

print("=== EMPRENDIMIENTOS TURÍSTICOS DE LLOA ===")
for i, emp in enumerate(emprendimientos_lloa, 1):
    print(f"\n--- EMPRENDIMIENTO {i} ---")
    print(f"TÍTULO: {emp['title']}")
    print(f"SUBTÍTULO: {emp['subtitle']}")
    print(f"DESCRIPCIÓN: {emp['description'][:100]}...")
    print("-" * 50)
