"""Categorías del directorio: una página de aterrizaje por oficio.

`match` son fragmentos (minúsculas, sin tildes) que se buscan en el nombre de
las profesiones del backend para decidir qué profesionales van en cada página.
Reglas de copy: español neutro (tuteo), sin guiones largos, sin hablar de IA.
"""

CATEGORIES = [
    {
        "slug": "pilates",
        "name": "Pilates",
        "singular": "profesor de pilates",
        "plural": "profesores de pilates",
        "match": ["pilates"],
        "title": "Profesores de pilates cerca de ti: clases y reservas",
        "description": "Encuentra instructoras e instructores de pilates en tu ciudad. Clases en estudio, al aire libre o a domicilio. Mira perfiles, reseñas y reserva desde la app.",
        "h1": "Profesores y profesoras de pilates",
        "lead": "Pilates en estudio, en casa o en el parque. Compara perfiles reales, revisa reseñas y reserva tu clase sin intermediarios.",
        "sections": [
            ("Cómo elegir a tu profesora de pilates", [
                "El pilates se enseña de formas muy distintas. Antes de reservar conviene tener claro qué buscas: recuperarte de una molestia, ganar fuerza de core, mejorar la postura o simplemente moverte con más conciencia.",
                "- **Formación y método:** pregunta qué certificación tiene y si trabaja pilates suelo (mat), con máquinas o con ambos.\n- **Tamaño del grupo:** en grupos de 4 a 8 personas la corrección es mucho más cercana que en clases de 20.\n- **Lesiones y embarazo:** una buena instructora te pregunta por tu historial antes de empezar y adapta los ejercicios.\n- **Lugar y horario:** estudio, domicilio, online o al aire libre. Elige lo que puedas sostener durante meses.",
            ]),
            ("Clases al aire libre y en espacios no convencionales", [
                "Muchas instructoras dan clases de pilates en parques, playas o terrazas cuando el clima acompaña. En Metriotes cada profesional indica si atiende de forma presencial, online o ambas, y publica la dirección de sus clases con enlace a Google Maps.",
            ]),
            ("Qué esperar de la primera clase", [
                "Una conversación breve sobre tu cuerpo y tus objetivos, ejercicios de respiración y activación, y una secuencia sencilla. No necesitas experiencia previa ni ropa especial: sí algo cómodo y una esterilla si la clase es de suelo.",
            ]),
        ],
        "faqs": [
            ("¿Cuánto cuesta una clase de pilates?", "Depende de la ciudad, del formato (grupal o individual) y del lugar. Cada profesional publica sus precios en su perfil de Metriotes, y muchos ofrecen bonos de varias clases con descuento."),
            ("¿Puedo hacer pilates si nunca he hecho ejercicio?", "Sí. Es una disciplina adaptable. Comunica a tu instructora tu punto de partida y cualquier lesión para que ajuste los ejercicios."),
            ("¿Es mejor pilates en grupo o clases individuales?", "Las clases individuales avanzan más rápido y se adaptan a lesiones. Las grupales son más económicas y motivan más. Muchas personas combinan ambas."),
            ("¿Cuántas veces por semana debería hacer pilates?", "Dos sesiones semanales suelen ser suficientes para notar cambios en postura y fuerza en pocas semanas. Lo importante es la constancia."),
        ],
        "articles": ["como-elegir-profesor-pilates", "clases-al-aire-libre-pilates-yoga"],
    },
    {
        "slug": "yoga",
        "name": "Yoga",
        "singular": "profesor de yoga",
        "plural": "profesores de yoga",
        "match": ["yoga"],
        "title": "Profesores de yoga cerca de ti: clases y reservas",
        "description": "Descubre instructoras e instructores de yoga en tu ciudad: hatha, vinyasa, yin y más. Perfiles verificados, reseñas reales y reservas desde la app.",
        "h1": "Profesores y profesoras de yoga",
        "lead": "Encuentra un estilo y una persona que te acompañe. Clases en estudio, al aire libre o desde casa.",
        "sections": [
            ("Estilos de yoga: cuál te conviene", [
                "- **Hatha:** ritmo pausado, posturas sostenidas. Ideal para empezar.\n- **Vinyasa:** secuencias fluidas coordinadas con la respiración. Más dinámico.\n- **Yin:** posturas largas y pasivas para soltar tensión y ganar flexibilidad.\n- **Restaurativo:** relajación profunda con apoyos. Pensado para el descanso del sistema nervioso.\n- **Yoga prenatal:** adaptado a cada trimestre del embarazo.",
            ]),
            ("Qué mirar en una instructora de yoga", [
                "Más que el estilo, importa cómo te hace sentir la clase. Fíjate en si explica alternativas para cada postura, si respeta tus límites y si el ambiente es amable. Las reseñas de otros alumnos en Metriotes te dan una idea antes de reservar.",
            ]),
            ("Yoga en el parque, en la playa o en tu casa", [
                "Cada profesional de Metriotes marca su modalidad (presencial, online o ambas) y publica dónde da las clases, con enlace al mapa. Así puedes encontrar quien practique cerca de ti o quien enseñe a domicilio.",
            ]),
        ],
        "faqs": [
            ("¿Qué tipo de yoga es mejor para empezar?", "Hatha o yoga suave suelen ser los más recomendables: ritmo lento y explicaciones claras de cada postura."),
            ("¿Necesito ser flexible para hacer yoga?", "No. La flexibilidad es una consecuencia de la práctica, no un requisito. Una buena instructora te ofrece variantes para tu nivel."),
            ("¿Qué necesito para mi primera clase?", "Ropa cómoda y, si la clase es presencial, una esterilla (muchas instructoras prestan una). Evita comer pesado una o dos horas antes."),
            ("¿Cuánto dura una clase de yoga?", "Lo habitual son 60 a 90 minutos. Cada profesional indica la duración de sus clases en su perfil."),
        ],
        "articles": ["clases-al-aire-libre-pilates-yoga", "como-empezar-yoga-guia-principiantes"],
    },
    {
        "slug": "meditacion-mindfulness",
        "name": "Meditación y mindfulness",
        "singular": "instructor de meditación",
        "plural": "instructores de meditación y mindfulness",
        "match": ["meditacion", "mindfulness"],
        "title": "Instructores de meditación y mindfulness",
        "description": "Encuentra instructores de meditación y mindfulness: talleres, clases grupales y acompañamiento individual, presencial u online. Reserva desde la app.",
        "h1": "Instructores de meditación y mindfulness",
        "lead": "Aprende a meditar con guía real, en grupo o de forma individual, y conviértelo en un hábito que dure.",
        "sections": [
            ("Meditación guiada o con instructor: la diferencia", [
                "Una app de audios es un buen punto de partida, pero un instructor te corrige la postura, resuelve dudas y te ayuda a sostener la práctica cuando se vuelve incómoda. Muchos programas de mindfulness duran ocho semanas con sesiones semanales.",
            ]),
            ("Qué buscar", [
                "- Formación específica (MBSR, mindfulness, tradiciones contemplativas).\n- Ritmo adecuado: sesiones cortas al inicio y progresión gradual.\n- Un enfoque laico y práctico si no buscas un marco espiritual.",
            ]),
        ],
        "faqs": [
            ("¿Cuánto tiempo al día debería meditar?", "Empezar con cinco a diez minutos diarios es más útil que una hora una vez por semana. La regularidad pesa más que la duración."),
            ("¿Meditar sirve para el estrés y la ansiedad?", "Puede ayudar a gestionar el estrés cotidiano. Si sientes que la ansiedad interfiere con tu vida, consulta además con un profesional de la salud mental."),
            ("¿Hay talleres para principiantes?", "Sí. Muchos instructores en Metriotes publican talleres y clases abiertas para quien empieza."),
        ],
        "articles": ["como-crear-habitos-que-duran"],
    },
    {
        "slug": "idiomas",
        "name": "Idiomas",
        "singular": "profesor de idiomas",
        "plural": "profesores de idiomas",
        "match": ["idiomas", "language"],
        "title": "Profesores de idiomas particulares: online y presencial",
        "description": "Encuentra profesores de idiomas particulares: inglés, francés, italiano, alemán y más. Clases online o en tu ciudad. Perfiles, reseñas y reserva en la app.",
        "h1": "Profesores de idiomas",
        "lead": "Clases particulares o en grupo con profesores reales, online o en tu ciudad. Elige por objetivo, nivel y horario.",
        "sections": [
            ("Cómo elegir un profesor de idiomas", [
                "- **Objetivo claro:** conversar para viajar, preparar un examen (DELE, IELTS, TOEFL, DELF), trabajar o mudarte. Cada meta pide un método distinto.\n- **Lengua materna o nivel nativo:** útil sobre todo para pronunciación y expresiones cotidianas.\n- **Estructura:** un buen profesor te propone un plan con hitos, no solo conversación libre.\n- **Frecuencia:** dos clases semanales de 60 minutos suelen ser un buen ritmo para avanzar.",
            ]),
            ("Clases individuales o grupales", [
                "Las individuales se adaptan a tu nivel y a tu horario. Las grupales son más económicas y obligan a hablar con otras personas. Algunos profesores ofrecen bonos de clases prepagadas, lo que reduce el precio por sesión.",
            ]),
            ("Online o presencial", [
                "Con clases online puedes elegir al mejor profesor sin importar la ciudad. Con clases presenciales ganas inmersión y conversación más natural. En Metriotes cada profesional indica si da clases online, presenciales o ambas.",
            ]),
        ],
        "faqs": [
            ("¿Cuánto cuesta una clase particular de idiomas?", "Varía según el idioma, la experiencia del profesor y la ciudad. Los precios están publicados en cada perfil y muchos profesores ofrecen una primera clase de prueba o bonos."),
            ("¿Cuánto tardo en hablar un idioma con soltura?", "Depende del idioma de partida, de la frecuencia y de cuánto practiques fuera de clase. Con constancia y conversación semanal, la mayoría nota un salto claro en pocos meses."),
            ("¿Puedo preparar un examen oficial con un profesor particular?", "Sí. Busca a alguien con experiencia en el examen concreto y pídele un plan por sesiones."),
        ],
        "articles": ["como-encontrar-profesor-idiomas-particular"],
    },
    {
        "slug": "psicologos",
        "name": "Psicología y terapia",
        "singular": "psicólogo",
        "plural": "psicólogos y terapeutas",
        "match": ["psicolog", "psicoterap", "terapeuta", "psiquiatr", "sexolog"],
        "title": "Psicólogos y terapeutas cerca de ti",
        "description": "Encuentra psicólogos, psicoterapeutas y terapeutas de pareja en tu ciudad o por videollamada. Revisa perfiles, especialidades y reseñas, y reserva desde la app.",
        "h1": "Psicólogos y terapeutas",
        "lead": "Un primer paso más fácil: perfiles claros, especialidades visibles y reserva de sesión en la misma app donde llevas tu proceso.",
        "sections": [
            ("Cómo elegir un psicólogo o psicóloga", [
                "- **Titulación y registro profesional:** verifica que sea psicólogo o psiquiatra habilitado en su país.\n- **Enfoque:** cognitivo conductual, sistémico, psicoanalítico, humanista. No hay uno mejor para todos; depende de tu caso y de con cuál conectes.\n- **Especialidad:** ansiedad, duelo, pareja, familia, trauma, adolescentes.\n- **Modalidad:** online o presencial. La terapia online funciona bien para muchas consultas.",
            ]),
            ("La primera sesión", [
                "Es un espacio para conocerse. Cuenta qué te trajo, qué esperas y pregunta cómo trabaja. Si no sientes conexión, es completamente válido probar con otro profesional.",
            ]),
            ("Si estás pasando un momento muy difícil", [
                "Metriotes no sustituye la atención en una crisis. Si tienes pensamientos de hacerte daño o sientes que estás en peligro, contacta con los servicios de emergencia de tu país o con una línea de ayuda de tu zona de inmediato.",
            ]),
        ],
        "faqs": [
            ("¿Qué diferencia hay entre psicólogo, psicoterapeuta y psiquiatra?", "El psicólogo estudia la conducta y los procesos mentales y realiza terapia. El psicoterapeuta es quien se ha especializado en terapia. El psiquiatra es médico y puede recetar medicación."),
            ("¿Cuánto dura una sesión de terapia?", "Lo habitual son 45 a 60 minutos, con una frecuencia semanal o quincenal al inicio."),
            ("¿La terapia online es tan efectiva como la presencial?", "Para muchas consultas, sí. La clave es la relación terapéutica, la privacidad del espacio y la constancia."),
            ("¿Mis datos están protegidos?", "Sí. Metriotes es privado por defecto y tú decides qué compartes con cada profesional."),
        ],
        "articles": ["como-elegir-psicologo-primera-sesion"],
    },
    {
        "slug": "coaching",
        "name": "Coaching y mentoría",
        "singular": "coach",
        "plural": "coaches y mentores",
        "match": ["coach", "mentor", "orientador"],
        "title": "Coaches y mentores: encuentra al tuyo",
        "description": "Coach de vida, ejecutivo, de hábitos, de carrera y mentores personales. Compara perfiles, enfoques y reseñas, y reserva tu primera sesión desde la app.",
        "h1": "Coaches y mentores",
        "lead": "Alguien que te ayude a ordenar lo que quieres, definir pasos concretos y sostenerlos en el tiempo.",
        "sections": [
            ("Qué hace un coach y qué no", [
                "Un coach trabaja con preguntas, estructura y seguimiento para que alcances un objetivo propio: cambio de carrera, hábitos, liderazgo, equilibrio de vida. No es terapia ni da diagnósticos. Si lo que necesitas es trabajar heridas o un trastorno, un psicólogo es el camino adecuado.",
            ]),
            ("Tipos de coaching", [
                "- **Coaching de vida:** claridad de valores, decisiones, equilibrio.\n- **Coaching ejecutivo y laboral:** liderazgo, transiciones de carrera, comunicación.\n- **Coaching de hábitos:** rutinas, energía, sueño, constancia.\n- **Coaching ontológico:** observa el lenguaje, las emociones y el cuerpo para generar nuevas acciones.",
            ]),
            ("Cómo elegir", [
                "Pide una sesión de prueba, pregunta por su método y por cómo mide el avance. Un buen coach acuerda objetivos contigo desde el inicio y revisa el progreso de forma explícita.",
            ]),
        ],
        "faqs": [
            ("¿Cuántas sesiones necesito?", "Un proceso suele durar entre 6 y 12 sesiones, aunque depende de la meta. Un buen coach te lo plantea desde la primera conversación."),
            ("¿Coaching y terapia son lo mismo?", "No. El coaching se orienta al futuro y a metas concretas. La terapia aborda malestar emocional y salud mental."),
            ("¿Puedo trabajar con un coach desde Metriotes?", "Sí. Puedes compartir tus objetivos con tu coach dentro de la app y tener el seguimiento en un solo lugar."),
        ],
        "articles": ["que-es-un-coach-de-vida", "como-crear-habitos-que-duran"],
    },
    {
        "slug": "nutricion",
        "name": "Nutrición",
        "singular": "nutricionista",
        "plural": "nutricionistas",
        "match": ["nutricion"],
        "title": "Nutricionistas cerca de ti: consulta y plan online",
        "description": "Encuentra nutricionistas en tu ciudad o por videollamada. Planes de alimentación personalizados que recibes y sigues dentro de la app. Reserva tu consulta.",
        "h1": "Nutricionistas",
        "lead": "Un plan de alimentación hecho para ti, que recibes en tu móvil y puedes seguir comida por comida.",
        "sections": [
            ("Qué esperar de una consulta de nutrición", [
                "La primera cita suele incluir historial clínico, hábitos, objetivos y medidas. Después, tu nutricionista diseña un plan que se ajusta a tu rutina, tus gustos y tus restricciones.",
            ]),
            ("Seguir el plan dentro de Metriotes", [
                "Con Metriotes, el profesional arma el plan semanal y te lo envía. Tú lo aceptas, marcas lo que comes y llevas el registro de tu peso, para llegar a la siguiente consulta con datos reales.",
            ]),
            ("Cómo elegir", [
                "- Titulación en nutrición y dietética y registro profesional vigente.\n- Enfoque: pérdida de peso, deporte, patologías, alimentación vegetariana, embarazo.\n- Evita promesas milagrosas o dietas extremas.",
            ]),
        ],
        "faqs": [
            ("¿Cada cuánto debo ir al nutricionista?", "Al inicio suele ser cada 2 a 4 semanas y luego se espacia a una vez al mes o menos."),
            ("¿Puedo hacer la consulta online?", "Sí. Muchos nutricionistas atienden por videollamada y trabajan el plan a través de la app."),
            ("¿Un plan de alimentación es lo mismo que una dieta?", "No. Un plan bien diseñado busca un cambio sostenible de hábitos, no una restricción temporal."),
        ],
        "articles": [],
    },
    {
        "slug": "entrenadores",
        "name": "Entrenamiento personal",
        "singular": "entrenador personal",
        "plural": "entrenadores personales",
        "match": ["entrenador", "preparador"],
        "title": "Entrenadores personales cerca de ti u online",
        "description": "Encuentra entrenadores personales y preparadores físicos. Rutinas ejercicio por ejercicio en la app, sesiones presenciales u online. Reserva tu primera sesión.",
        "h1": "Entrenadores personales",
        "lead": "Rutinas hechas para tu nivel y tu objetivo, con seguimiento real de cada entrenamiento.",
        "sections": [
            ("Qué debe incluir un buen entrenamiento personal", [
                "- Una evaluación inicial (historial, lesiones, objetivos, nivel).\n- Progresión: la carga aumenta de forma planificada, semana a semana.\n- Técnica por delante de peso. Un buen entrenador corrige.\n- Seguimiento: registrar series, repeticiones y cargas para medir mejora.",
            ]),
            ("Tu rutina en la app", [
                "Con Metriotes, tu entrenador te envía la rutina por días y ejercicios. Registras cada serie durante el entrenamiento y él ve tu avance sin que tengas que mandar capturas ni mensajes.",
            ]),
        ],
        "faqs": [
            ("¿Cuántas veces por semana debería entrenar?", "Entre 2 y 4 sesiones semanales funcionan para la mayoría de objetivos. Tu entrenador lo ajusta a tu nivel y tu disponibilidad."),
            ("¿Es mejor entrenamiento presencial u online?", "El presencial corrige técnica en directo. El online es más flexible y económico si ya sabes ejecutar los ejercicios. Algunos combinan ambos."),
            ("¿Sirve para quien nunca ha entrenado?", "Sí. Empezar con un profesional evita lesiones y malos hábitos."),
        ],
        "articles": [],
    },
    {
        "slug": "fisioterapia",
        "name": "Fisioterapia y terapias manuales",
        "singular": "fisioterapeuta",
        "plural": "fisioterapeutas, osteópatas y quiroprácticos",
        "match": ["fisioterap", "osteopat", "quiropract"],
        "title": "Fisioterapeutas y osteópatas cerca de ti",
        "description": "Encuentra fisioterapeutas, osteópatas y quiroprácticos en tu ciudad. Perfiles claros, reseñas de pacientes y reserva de cita desde la app.",
        "h1": "Fisioterapeutas, osteópatas y quiroprácticos",
        "lead": "Cuida tu cuerpo con profesionales de tu zona y reserva tu cita de forma sencilla.",
        "sections": [
            ("Cuándo ir a cada especialista", [
                "El **fisioterapeuta** trata lesiones, dolores musculares y rehabilita tras una operación. El **osteópata** trabaja con técnicas manuales sobre el conjunto del cuerpo. El **quiropráctico** se centra en la columna y las articulaciones. Ante un dolor intenso o persistente, consulta primero con tu médico.",
            ]),
        ],
        "faqs": [
            ("¿Necesito derivación médica?", "Depende del país y del seguro. Para consulta privada normalmente no, pero ante un dolor intenso conviene un diagnóstico médico previo."),
            ("¿Cuántas sesiones se necesitan?", "Depende de la lesión. El profesional te dará un plan estimado tras la primera valoración."),
        ],
        "articles": [],
    },
    {
        "slug": "musica-arte-danza",
        "name": "Música, arte y danza",
        "singular": "profesor",
        "plural": "profesores de música, arte y danza",
        "match": ["musica", "arte", "danza", "ajedrez"],
        "title": "Profesores de música, arte y danza: clases",
        "description": "Clases de música, dibujo, pintura, danza y ajedrez con profesores independientes. Presenciales u online. Encuentra el tuyo y reserva desde la app.",
        "h1": "Profesores de música, arte y danza",
        "lead": "Aprende un instrumento, retoma el dibujo o súmate a una clase de baile con profesores independientes de tu ciudad.",
        "sections": [
            ("Clases particulares o talleres", [
                "Las clases particulares avanzan a tu ritmo. Los talleres y las clases grupales son una forma amable de probar y conocer gente con tus mismos intereses.",
            ]),
        ],
        "faqs": [
            ("¿Hay límite de edad para aprender?", "No. Se puede empezar un instrumento, una técnica de arte o un baile a cualquier edad."),
            ("¿Necesito material propio?", "Depende de la disciplina. Pregunta al profesor antes de la primera clase; muchos lo indican en su perfil."),
        ],
        "articles": [],
    },
]


def by_slug(slug):
    for c in CATEGORIES:
        if c["slug"] == slug:
            return c
    return None
