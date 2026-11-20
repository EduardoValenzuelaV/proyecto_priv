/* ============================================================
   CONFIGURACIÓN
   ============================================================ */
const URL_BACKEND = '';
const FECHA_INICIO = '2026-10-17';
// Aviso de visitas por ntfy.sh: suscríbete a este tema en la app ntfy. Vacío = sin aviso.
const NTFY_TEMA = 'dallana-aviso-0232a591a0';

/* Versión corta anterior de la carta (conservada como referencia local).
const CARTA_LOCAL_CORTA = `Para mi Dallana 💙

Nuestro primer mes

Un mes. Dicho así parece poco, pero cuando miro hacia atrás siento que han pasado muchas cosas, y quería dejarlas por escrito para que algún día puedas volver a leer esto y acordarte de cómo empezó todo.

Te escribo porque desde que te conozco no paro de encontrar cosas que me gustan de ti, y quería que vieras lo que yo veo cuando te miro.

Tu sonrisa me desarma, eso ya lo sabes. Pero lo que más me tiene así es tu forma de ser: cómo defiendes lo que piensas, lo tierna que puedes ser y, al rato, lo payasa. Me encanta escucharte hablar. Cada vez que conversamos me quedo con ganas de saber más de ti, y creo que eso es lo que más me gusta: que no me canso de conocerte.

Me gustan hasta las cosas más raras. Que te gusten las Nik de chirimoya alegre. Que comas por colores y lo defiendas con tanta lógica que casi me convences (casi). Que cantes tan bonito, sobre todo cuando cantas [canción]. Que puedas estar hablándome con toda la pasión del mundo sobre [tema que le apasiona] y de repente salirme con una tontera que me hace reír. Seguramente para ti son detalles, pero para mí son las cosas que hacen que me encante estar contigo.

El 31 de octubre lo tengo guardado como uno de mis días favoritos. Nos reímos muchísimo, comimos [qué comieron] y terminamos viendo las películas de los Minions y esa parodia de terror jsjsj. No hicimos nada del otro mundo, y aun así fue una de las mejores noches que he tenido. Ahí me di cuenta de que lo que más me gusta de cualquier plan es que estés tú.

Y hay una frase tuya que no se me olvida: «Tú eres mi Arauco y yo soy tu Talca». No la voy a explicar, porque es nuestra y así está bien. Solo te digo que cada vez que me acuerdo, sonrío.

Gracias por preocuparte de cómo amanecí, de si llegué bien o de si comí. Gracias por alegrarte cuando algo me sale bien. Cuando me dijiste que estabas demasiado orgullosa de mí, no te imaginas lo que significó leer eso. Y yo también estoy muy orgulloso de ti, de cómo te esfuerzas y de cómo cuidas a la gente que quieres.

Conmigo siempre vas a tener a alguien que te escuche. En los días buenos, obvio, pero también en los malos, en esos en que ni tú misma sabes bien qué te pasa y lo único que necesitas es un abrazo largo. No tienes que estar siempre bien conmigo ni fingir que lo estás. Yo quiero estar contigo en todas, no solo en las fáciles.

Ojalá pudieras mirarte como yo te miro. No solo por lo bonita que eres o por lo bien que te queda tu forma de vestir, sino por cómo te brillan los ojos cuando algo te emociona. No tienes que ser perfecta ni demostrarme nada. Me gustas tal como eres, y no quiero que cambies eso por nada.

No te voy a prometer que todo va a ser perfecto, pero sí que siempre voy a escucharte, respetarte y estar aquí para ti. Y que voy a seguir haciendo lo posible por sacarte esa risa, porque es de mis cosas favoritas.

Todavía nos queda tanto por vivir juntos, tantas conversaciones, tantas risas y un montón de momentos que ni siquiera imaginamos. Una vez me dijiste que íbamos a tener un futuro muy bonito juntos. Lo dijiste tan segura que me lo creí, y hasta ahora no me has dado ninguna razón para dudarlo.

Gracias por este primer mes, por todo lo que nos hemos reído y por dejarme conocerte. Es solo el comienzo, y ya es de las mejores cosas que me han pasado.

Si tuviera que elegir de nuevo con quién empezar esto, no lo pensaría ni un segundo: te elegiría a ti otra vez.

Feliz primer mes, mi Dallana. Estoy enamorado de ti, y cada día un poquito más.

Te quiero muchísimo, mi niña bonita 💙`;
*/

const CARTA_LOCAL = `Para mi Dallana 💙

Nuestro primer mes juntos

Un mes. Dicho así parece poco, y sin embargo, cuando miro hacia atrás, siento que en estas semanas he vivido muchas cosas bonitas que quiero guardar para siempre. Quizás por eso quise escribirte esta carta: para dejar en palabras un poquito de todo lo que has significado para mí durante este tiempo y para que algún día puedas volver a leerla y recordar lo bonito que ha sido comenzar esta historia juntos.

No escribo esta carta para convencerte de lo maravillosa que eres. La escribo porque, desde que te conozco, he encontrado cada vez más razones para admirarte, y quería que pudieras ver, aunque fuera un poquito, lo que yo veo cuando te miro.

Hay muchas cosas de ti que me han ido enamorando, y aunque tu sonrisa tiene una manera especial de desarmarme, no es lo único que me hace mirarte con tanta admiración. Me enamora tu forma de ser, la manera en que te expresas, cómo defiendes lo que piensas y esa combinación tan bonita entre tu ternura, tu carácter y tu lado divertido. Me encanta escucharte hablar y sorprenderme con cada ocurrencia tuya. Contigo siempre hay algo nuevo que despierta mi curiosidad, y creo que eso es lo que más me gusta: que no me canso de conocerte. Cada conversación me deja con ganas de saber un poquito más de ti, de tus gustos, de tus historias y de todas esas pequeñas cosas que te hacen ser la persona de la que me estoy enamorando cada dia más.

Y esa curiosidad también aparece en los detalles más pequeños. Me gusta descubrir más cosas hermosas que te hacen ser tú: como que te gusta las Nik de chirimoya alegre , que comas por colores y lo defiendas con tanta lógica que casi consigues convencerme, que cantes tan bonito (Soy tu Fan N°1) y que puedas pasar de hablarme con toda la pasión del mundo sobre algo que te gusta a decirme alguna tontería que termina sacándome una sonrisa. Quizás para ti sean detalles pequeños, pero para mí forman parte de todo aquello que hace que me encante estar contigo. Sé que todavía me queda muchísimo por conocer de ti, de tus historias, tus sueños, tus pensamientos y de todas esas partes de tu vida que poco a poco irás compartiendo conmigo. Y sinceramente, me hace muchasima ilusión descubrirlas.

Hay un recuerdo que le tengo muchisimo cariño: el dia 31 de octubre. Todavía me acuerdo de lo mucho que nos reímos, de las cosas ricas que compartimos,  de cómo terminamos viendo aquellas películas de los Minions y esa parodia de terro jsjsj. No sé si tú la recuerdas con la misma emoción que yo, pero para mí fue una de esas noches que se quedan guardadas como un recuerdo muy espcial que tengo contigo. No hubo necesidad de hacer nada extraordinario; simplemente disfruté de compartir ese tiempo contigo. Y creo que ahí entendí algo que cada vez tengo más claro: mi parte favorita de muchos planes no es lo que hacemos, sino que seas tú quien está a mi lado.

También hay una frase tuya que se quedó guardada  de mi corazón: «Tú eres mi Arauco y yo soy tu Talca». No voy a intentar explicar lo que significa, porque siento que perdería un poquito de su magia. Es una de esas cosas que son nuestras, que quizás nadie más entendería de la misma manera. Solo quiero que sepas que la recuerdo con muchísimo cariño y que cada vez que pienso en ella me hace sonreír.

Quiero agradecerte también por todas esas pequeñas cosas que haces y que quizás no siempre notas. Por preocuparte de cómo amanecí, de si llegué bien ; por interesarte en mis proyectos y alegrarte sinceramente cuando algo me sale bien. Recuerdo especialmente cuando me dijiste que estabas demasiado orgullosa de mí. Quizás no imaginas lo bonito que fue leer esas palabras y sentir que alguien a quien quiero tanto se alegra de verme avanzar. Son detalles que valoro muchísimo, porque me hacen sentir querido y acompañado. Y quiero que sepas que yo también estoy muy orgulloso de ti: de tus esfuerzos, de tus logros, de tus metas y de esa manera tan tuya de enfrentar las cosas y preocuparte por las personas que quieres.

Quiero que sepas que conmigo siempre tendrás a alguien dispuesto a escucharte, alguien con quien puedas compartir tus pensamientos, tus alegrías, tus preocupaciones y hasta esas cosas que a veces cuesta poner en palabras. Me gustaría conocerte también en esos momentos en los que no sabes muy bien qué sientes o simplemente necesitas un abrazo y un poquito de compañía. No espero que siempre tengas una sonrisa ni que todos tus días sean buenos; quiero compartir contigo los días bonitos, pero también acompañarte en los momentos dificiles . Y deseo que tú también encuentres en mí esa confianza, que nunca tengas miedo de decirme lo que piensas o sientes.
Ojalá algún día pudieras mirarte con un poquito de la ternura con la que yo te miro. Y no me refiero solamente a lo bonita que te ves en una foto, o tu hermosa sonrisa o a lo bien que te queda ese estilo  de vesir  que tienes y que tanto me gusta. Me refiero también  cuando te emocionas hablando de algo que te apasiona, cuando cantas, cuando defiendes tus ideas o cuando tienes alguno de esos gestos tan tuyos con las personas que quieres. Hay tantas cosas bonitas en ti que van mucho más allá de lo que se puede ver a simple vista. No tienes que ser perfecta ni demostrarme nada para merecer mi cariño. No quiero que cambies tu esencia para encajar en ninguna parte. Me gusta quién eres, con tu personalidad,  tus ideas y esa forma tan bonita que tienes de ser.

No voy a prometerte que todos los días serán perfectos, porque sé que la vida no funciona así. Pero sí quiero prometerte algo que está en mis manos:  siempre voy a escucharte, respetarte y  sobre todo siempre estare aqui para ti . Y por supuesto, voy a seguir intentando hacerte sonreír, porque verte feliz y escuchar esa risa tuya es una de mis cosas favoritas en este mundo.

Nos quedan tantas películas por ver, caminatas tranquilas, comidas por compartir, canciones por descubrir y momentos que todavía ni siquiera imaginamos. Quiero acompañarte en tus proyectos, celebrar tus logros, escuchar tus historias y seguir descubriendo todo aquello que te hace ilusión. Como me dijiste con tanta dulzura, tendremos un hermoso futuro juntos. No sé exactamente qué nos espera en cada capítulo, pero me encanta pensar que todavía tenemos tantas páginas por escribir y que puedo descubrirlas a tu lado, sin prisa y disfrutando de cada etapa.

Gracias por este primer mes, por tus risas, tus abrazos, tus conversaciones, tus ocurrencias y por dejarme conocer un poquito más de ti. Gracias por compartirme tus días, tus pensamientos y esos pequeños mundos que forman parte de quien eres. Me hace muy feliz saber que estamos construyendo algo bonito y que, entre tantas personas, tengo la suerte de poder llamarte mi Amor.

Y si este primer mes me ha enseñado algo, es que todavía me queda muchísimo de ti por descubrir. Qué suerte la mía jsjsjs, porque tengo la ilusión de seguir conociéndote, de enamorarme de tus pequeñas particularidades y de encontrar nuevas razones para admirarte. No quiero dejar de sorprenderme contigo ni de conquistarte en los pequeños detalles de cada día.

Feliz primer mes, mi Dallana.

Estoy enamorado de ti, de tu forma de ser y de todo eso que te hace tan especial para mí. 
Te quiero muchísimo, mi niña Hermosa . 💙

Con todo mi amor,

Tu Amorcito.`;
const API_DISPONIBLE = (
  (URL_BACKEND.startsWith('https://') && !URL_BACKEND.includes('tu-api-en-render')) ||
  URL_BACKEND.startsWith('http://localhost') ||
  URL_BACKEND.startsWith('http://127.0.0.1')
);

/* ============================================================
   CONTENIDO LOCAL
   ============================================================ */
const CONTENIDO_LOCAL = {
  cartas: [
    {titulo:"Ábreme cuando estés triste",mensaje:" si estás leyendo esto es porque algo te duele, y me gustaría estar ahí ahora mismo para abrazarte fuerte y no soltarte. No voy a decirte que no estés triste, porque tienes derecho a sentirte así. Solo quiero que sepas que no estás sola, ni ahora ni nunca. No tienes que explicarme nada ni tener las palabras correctas. Llora si lo necesitas, y después escríbeme, aunque sea solo un “estoy mal”. Yo voy a entender. Y cuando esto pase, porque va a pasar, voy a seguir aquí, igual que hoy."},
    {titulo:"Ábreme cuando no te sientas bonita",mensaje:"Sé que hay días en que te miras al espejo y no te gusta lo que ves. Me da pena, porque yo te miro todos los días y no me canso de ver lo Hermosa que eres. Pero lo que más me gusta de ti no sale en ninguna foto: es cómo te brillan los ojos cuando hablas de algo que amas, cómo te ríes de tus propias tonteras, cómo cantas cuando crees que nadie te escucha. Hoy, si no puedes creerlo tú, créeme a mí: eres la mujer mas hermosa de mi mundo."},
    {titulo:"Ábreme cuando dudes de ti misma",mensaje:"Ya sé, esa vocecita que te dice que no eres suficiente. Yo también la conozco. Pero déjame contarte lo que yo veo: una mujer que estudia algo difícil porque le apasiona, que defiende lo que piensa aunque cueste, que no se rinde fácil. Todo lo que has logrado hasta ahora lo hiciste tú, con tu esfuerzo y tu cabeza. Esa voz miente. Y si hoy no te crees capaz, no pasa nada: yo creo en ti por los dos hasta que vuelvas a verlo."},
    {titulo:"Ábreme cuando tengas un mal día",mensaje:" No tienes que arreglarlo todo hoy. Date permiso de que sea un mal día y nada más. Come algo rico, ponte cómoda, y si quieres contarme todo con lujo de detalles, aquí estoy para escucharte y enojarme contigo con lo que sea que te haya pasado. Mañana vas a despertar y esto se va a ver más chiquito. Mientras tanto, te mando el abrazo más largo que puedas imaginar."},
    {titulo:"Ábreme cuando sientas que no puedes más",mensaje:"Para. Respira conmigo un segundo. No tienes que poder con todo, y no tienes que hacerlo sola. Sé que eres fuerte, pero ser fuerte no significa aguantarlo todo calladita. A veces ser fuerte es decir “necesito ayuda”. Así que hoy te pido algo: descansa, apóyate en mí, en tu familia, en la gente que te quiere. Llámame, a la hora que sea, de verdad. Nada de lo que tengas pendiente vale más que tú. Lo que importa ahora es que estés bien, y yo quiero ayudarte a llegar ahí."},
    {titulo:"Ábreme cuando estés orgullosa de ti",mensaje:"Mírate Te lo dije, o no? Sabía que ibas a poder. Quiero que te quedes un ratito con esta sensación y la disfrutes, porque te costó y te la ganaste. A veces pasas tan rápido a lo siguiente que no te das tiempo de celebrar, así que hoy celebra. Yo estoy feliz, orgulloso, emocionado, todo junto. Y una vez me dijiste que estabas demasiado orgullosa de mí; hoy me toca a mí decírtelo a ti: estoy demasiado orgulloso de ti, mi amor."},
    {titulo:"Ábreme cuando necesites recordar cuánto vales",mensaje:"Quiero que leas esto despacito. Vales muchísimo, y no lo digo por decir. No vales por tus notas, ni por lo que logras, ni por lo que piensen los demás. Vales porque eres tú:  defiendes lo que crees aunque cueste, porque tienes un corazón enorme que a veces ni tú misma ves. Si alguien te hizo sentir menos, se equivocó. Si fuiste tú misma, te pido que te trates con la misma ternura con la que tratas a los demás. Tú mereces todo lo bonito que le das al mundo, y yo voy a estar aquí para recordártelo cada vez que se te olvide."},
    {titulo:"Ábreme cuando simplemente quieras sonreír",mensaje:"Ok, cierra los ojos un segundo y acuérdate: tú, súper seria,  Nosotros la noche del 31, muertos de la risa con esa parodia de terror. ¿Ya sonreíste? Si no, aquí va otra: en este mismo momento, en algún lugar, hay un tonto enamorado de ti pensando en lo afortunado que es. Ese soy yo. Tú eres mi Talca y yo soy tu Arauco, para siempre. Te Amo mi Amor. 💙"}
  ],
  museo: [
    {titulo:'Tu vocación',descripcion:'Tu curiosidad por la geología y la dedicación que pones en tu carrera me inspiran.',mensaje:'Mi geóloga favorita.',foto:''},
    {titulo:'Tu sonrisa',descripcion:'Tu sonrisa tiene el poder de arreglarme el día, aunque venga malo.',mensaje:'Mi lugar favorito del mundo.',foto:''},
    {titulo:'Tus gustos',descripcion:'Sushi, pizza , Turrones y esos momentos simples que disfrutamos juntos.',mensaje:'Me gusta aprender qué cosas te hacen feliz.',foto:''},
    {titulo:'Nuestros paseos',descripcion:'Caminar contigo por Conce siempre es un buen plan.',mensaje:'A tu lado, cualquier camino se vuelve mi favorito.',foto:''},
    {titulo:"Tu voz",descripcion:"Me encanta escucharte cantar; podría quedarme horas así.",mensaje:"Mi cantante favorita.",foto:''},
    {titulo:"Tu manera de cuidar",descripcion:"Siempre te preocupas de si llegué bien, de si comí, de cómo amanecí.",mensaje:"Me haces sentir muy querido.",foto:''},
    {titulo:"Tu carácter",descripcion:"Defiendes lo que piensas con seguridad, y eso me encanta de ti.",mensaje:"Nunca dejes de hacerlo.",foto:''},
    {titulo:"Tu lado divertido",descripcion:"Pasas de hablar súper en serio a decir una tontera en segundos.",mensaje:"Contigo me río de verdad.",foto:''},
    {titulo:"Tu estilo",descripcion:"Me encanta tu forma de vestir; tiene algo muy tuyo.",mensaje:"Siempre te ves muy pero muy linda.",foto:''},
    {titulo:"Tus ojitos hermosos",descripcion:"Podría quedarme mirándolos por horas; dicen todo lo que sientes sin que hables.",mensaje:"Me pierdo en ellos cada vez.",foto:''},
    {titulo:"La mejor cocinera del mundo",descripcion:"Todo lo que cocinas sabe a cariño, y eso no se aprende en ninguna receta.",mensaje:"Mi chef favorita, sin discusión.",foto:''}
  ],
  autoestima: [
    {texto:'Eres valiente, incluso en los días difíciles.'},
    {texto:'Tu bondad marca la diferencia en quienes te rodean.'},
    {texto:'Mereces todo el cariño del mundo.'}
  ],
  frasco: [
    'Un abrazo cuando lo necesites.',
    'Una sonrisa para alegrar tu día.',
    'Recuerda que eres importante.'
  ],
  suenos: [
    {id:'sueno-1',titulo:'Conocer un lugar nuevo',descripcion:'',hecho:false},
    {id:'sueno-2',titulo:'Ver una película juntos',descripcion:'',hecho:false},
    {id:'sueno-3',titulo:'Salir a caminar sin apuro',descripcion:'',hecho:false}
  ]
};

const RESPALDO = [
 // Para reírse
  'Alerta: hay alguien sonriendo como tonto mientras piensa en ti. (Soy yo.)',
  'Contigo hasta esperar la micro se vuelve una aventura.',
  'Ranking oficial de mis cosas favoritas: 1. Tú. 2. Tú cantando. 3. Tú comiendo. 4. Lo demás.',
  'Estado actual: pensando en ti. Estado anterior: pensando en ti. Próximo estado: adivina.',
  'Tus ojitos deberían venir con advertencia: puede causar enamoramiento severo.',
  'Tengo una teoría: tu sonrisa debería estar prohibida. Es un peligro para mi concentración.',
  'Tú estudias rocas, yo estudio tus sonrisas. Los dos somos muy dedicados.',
  'Me encanta cuando defiendes tus ideas. Aunque a veces pierda yo. Bueno, casi siempre.',
  'Cuando cocinas no sé si me enamoro de la comida o de la cocinera. Bueno, sí sé.',
  'Mapa actualizado: Arauco sigue extrañando a Talca.',
  'Nivel de enamoramiento hoy: más que ayer, menos que mañana.',
  'Desde que te conozco sonrío mirando el celular. La gente ya me mira raro, y es tu culpa.',
  'Te prohíbo dudar de ti hoy. Firmado: tu amorcito, con toda la autoridad del mundo.',
  'Gracias por existir. En serio. Dale las gracias a tu mamá de mi parte.',
  'Si sonreíste, misión cumplida. Si no, aprieta otra vez, que tengo más.',
  // Tiernitos
  'Hoy no tengo nada profundo que decirte. Solo que eres linda. Muy linda. Demasiado.',
  'Cierra los ojos e imagina un abrazo gigante. Listo, ese era mío.',
  'Eres mi notificación favorita.',
  'Me sé de memoria cómo te ríes, y es de las cosas que más me gusta saber.',
  'Me gusta tu estilo. Y no hablo solo de cómo te vistes.',
  'Te debo tantos abrazos que perdí la cuenta. Te los voy a pagar todos, con intereses.',
  'Cuando sale una foto tuya sonriendo, yo la miro unas mil veces. Mínimo.',
  'Hoy te quiero así, tal cual: con tus ocurrencias, tus tonteras y esa sonrisa.',
  'Si fueras una canción, te tendría en repetición todo el día. Ah, espera, ya lo hago contigo.',
  'Mensaje del futuro: seguimos juntos y te sigues riendo igual de bonito.',
  'De todas mis notificaciones, las tuyas son las únicas que abro corriendo.',
  'Si alguna vez te sientes poca cosa, acuérdate de que hay alguien que se emociona porque le respondiste un mensaje.',
  'Te quiero linda, eso era todo. 💙',
  'Noticia de último minuto: Dallana sigue siendo la más linda. Seguiremos informando.',
  'Si me preguntan qué hago en mi tiempo libre, la respuesta honesta es: pensar en ti.',
  'Estoy haciendo una lista de tus defectos. Por ahora va en blanco. Seguiré buscando.',
  'Querida Dallana: este mensaje no tiene ningún propósito más que interrumpir tu día para decirte que te quiero.',
  'Dicen que no se puede tener todo en la vida. Claramente no te conocían.',
  'Mi celular ya sabe escribir tu nombre solo. Hasta él se dio cuenta de lo que me pasa.',
  'Si fueras una tarea, serías la única que haría con gusto y antes de tiempo.',
  'Te quiero más que tú a las Nik. Sí, sé que es mucho decir.',
  'Encuesta rápida: ¿quién es la más bonita? a) Dallana b) Dallana c) Todas las anteriores.',
  'Advertencia: este botón puede causar sonrisas incontrolables. Úsalo con responsabilidad.',
  'Tengo un problema: cada vez que me dices "amor", se me olvida lo que iba a decir.',
 
  'Si alguien te hace enojar hoy, avísame. No voy a hacer nada, pero te voy a dar la razón.',
  'Opinión científica de un no-geólogo: tú eres la roca más bonita de toda la corteza terrestre.',
  'Me robaste el corazón y no pienso poner denuncia.',
  'Si tuviera que describirte en una palabra, no podría. Me faltan palabras y me sobran sonrisas.',
  'Dato: la probabilidad de que esté pensando en ti ahora mismo es de un 99%. El 1% es cuando duermo. Y ahí sueño contigo.',
  'Tu risa debería venderse en farmacias. Cura cualquier cosa.',
  'Ya revisé y sí: sigues siendo mi persona favorita. Revisión diaria, resultado siempre igual.',
  'Hoy te mereces un premio. ¿Por qué? Por ser tú. Premio: este mensaje. Y un beso cuando nos veamos.',
  'Si te sientes cansada, imagina que te estoy haciendo cariño en el pelo.',
  'Mi superpoder secreto: reconocer tu risa en cualquier parte.',
  'Te aviso que hoy estás especialmente linda. No sé cómo lo sé, pero lo sé.',

].map((mensaje,i)=>({id:`offline-${i+1}`,mensaje,foto:''}));

const PLAYLIST = [
  {nombre:'Taylor Swift - Love Story', archivo:'Taylor Swift - Love Story.mp3'},
  {nombre:'The Weeknd, Ariana Grande - Die For You (Remix Lyric Video)', archivo:'The Weeknd, Ariana Grande - Die For You (Remix Lyric Video).mp3'},
  {nombre:'The Weeknd & Ariana Grande - Save Your Tears (Remix) (Official Video)', archivo:'The Weeknd & Ariana Grande - Save Your Tears (Remix) (Official Video).mp3'},
  {nombre:'Swedish House Mafia and The Weeknd - Moth To A Flame (Official Video)', archivo:'Swedish House Mafia and The Weeknd - Moth To A Flame (Official Video).mp3'},
  {nombre:'Billie Eilish - CHIHIRO (Official Music Video)', archivo:'Billie Eilish - CHIHIRO (Official Music Video).mp3'},
  {nombre:'Nessa Barrett - die first (official music video)', archivo:'Nessa Barrett - die first (official music video).mp3'},
  {nombre:'Billie Eilish - BIRDS OF A FEATHER (Official Music Video)', archivo:'Billie Eilish - BIRDS OF A FEATHER (Official Music Video).mp3'},
  {nombre:'The Verve - Bitter Sweet Symphony', archivo:'The Verve - Bitter Sweet Symphony.mp3'},
  {nombre:'New West - Those Eyes (Chapter 1)', archivo:'New West - Those Eyes (Chapter 1).mp3'}
];

/* ============================================================
   HELPERS
   ============================================================ */
const $ = id => document.getElementById(id);
const leerJSON = (key, fallback) => { try { return JSON.parse(localStorage.getItem(key) || 'null') || fallback; } catch { return fallback; } };
const leerSet = key => { try { return new Set(JSON.parse(localStorage.getItem(key) || '[]').map(String)); } catch { return new Set(); } };
const guardarSet = (key, set) => { try { localStorage.setItem(key, JSON.stringify([...set])); } catch {} };
const guardarJSON = (key, value) => { try { localStorage.setItem(key, JSON.stringify(value)); } catch {} };
// Los saludos de mañana/noche no son recuerdos: no cuentan para desbloquear la carta.
const esSaludo = id => String(id).startsWith('saludo-');
const vibrar = () => { if (navigator.vibrate) navigator.vibrate([30, 20, 42]); };

/* ============================================================
   ESTADO
   ============================================================ */
let contenido = CONTENIDO_LOCAL;
// Copia completa del contenido del servidor (incluye colecciones que esta página
// ya no muestra) para no borrarlas al guardar desde el panel.
let contenidoServidor = null;
let currentId = null;
let currentMensaje = '';
let token = '';
let mensajes = [];
let seen = new Set([...leerSet('dallanaSeen')].filter(id => !esSaludo(id)));
let favorites = leerSet('dallanaFavorites');
// Texto de cada favorito, para poder mostrarlo aunque venga de la API.
let favoriteTexts = leerJSON('dallanaFavoriteTexts', {});
let toquesSecretos = 0;

/* ============================================================
   POLYFILL dialog
   ============================================================ */
if (!HTMLDialogElement.prototype.showModal) {
  HTMLDialogElement.prototype.showModal = function () { this.setAttribute('open', ''); };
  HTMLDialogElement.prototype.close = function () { this.removeAttribute('open'); };
}

/* ============================================================
   CORAZONES FLOTANTES
   ============================================================ */
const heartDrift = $('heartDrift');
if (heartDrift && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const heartColors = ['#e0303f', '#3d72c4', '#4f9a4a', '#ff5a5f', '#6fa0e8', '#7cc46a'];
  const bienvenidaAbierta = () => { const w = $('welcome'); return !!w && !w.classList.contains('closed'); };
  function lanzarCorazon() {
    const enBienvenida = bienvenidaAbierta();
    const heart = document.createElement('span');
    heart.className = 'drift-heart';
    heart.textContent = '♥';
    // En la bienvenida suben por toda la pantalla; en la página, por los costados para no tapar el contenido
    const lado = enBienvenida ? Math.random() * 96
      : (Math.random() < .5 ? 1 + Math.random() * 15 : 84 + Math.random() * 14);
    heart.style.setProperty('--side', `${lado}vw`);
    heart.style.setProperty('--heart-color', heartColors[Math.floor(Math.random() * heartColors.length)]);
    heart.style.setProperty('--heart-size', `${16 + Math.random() * (enBienvenida ? 26 : 18)}px`);
    heart.style.setProperty('--heart-duration', `${7 + Math.random() * 5}s`);
    heart.style.setProperty('--heart-opacity', `${(enBienvenida ? .55 : .42) + Math.random() * .3}`);
    heart.style.setProperty('--heart-drift', `${-30 + Math.random() * 60}px`);
    if (heartDrift.childElementCount >= (enBienvenida ? 24 : 14)) heartDrift.firstElementChild.remove();
    heartDrift.append(heart);
    heart.addEventListener('animationend', () => heart.remove(), { once: true });
    setTimeout(() => heart.remove(), 13000);
  }
  for (let i = 0; i < 6; i++) setTimeout(lanzarCorazon, i * 350);
  let pulso = 0;
  setInterval(() => { pulso++; if (bienvenidaAbierta() || pulso % 2 === 0) lanzarCorazon(); }, 750);
}

/* ============================================================
   FECHA / CONTADOR
   ============================================================ */
function actualizarContador() {
  const [anio, mes, dia] = FECHA_INICIO.split('-').map(Number);
  const ahora = new Date();
  const inicio = Date.UTC(anio, mes - 1, dia);
  const hoy = Date.UTC(ahora.getFullYear(), ahora.getMonth(), ahora.getDate());
  const diferencia = Math.round((hoy - inicio) / 864e5);
  const el = $('counter'); if (!el) return;
  el.textContent = diferencia < 0
    ? `Faltan ${Math.abs(diferencia)} días para comenzar 💕`
    : `${diferencia + 1} ${diferencia === 0 ? 'día' : 'días'} juntos 💕`;
}

/* ============================================================
   PROGRESO Y CELEBRACIÓN
   ============================================================ */
function lanzarCelebracion() {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const container = $('celebrationContainer');
  if (!container) return;
  const simbolos = ['♥', '❀', '✿', '✧', '♡'];
  const colores = ['#e0303f', '#ff5a5f', '#3d72c4', '#6fa0e8', '#4f9a4a', '#f2c14e'];
  for (let i = 0; i < 40; i++) {
    const el = document.createElement('span');
    el.className = 'celebration-petal';
    el.textContent = simbolos[Math.floor(Math.random() * simbolos.length)];
    el.style.left = `${Math.random() * 100}vw`;
    el.style.color = colores[Math.floor(Math.random() * colores.length)];
    el.style.fontSize = `${14 + Math.random() * 22}px`;
    el.style.setProperty('--fall-duration', `${2.8 + Math.random() * 2.4}s`);
    el.style.setProperty('--drift-x', `${-60 + Math.random() * 120}px`);
    el.style.setProperty('--rot', `${-180 + Math.random() * 360}deg`);
    setTimeout(() => {
      container.append(el);
      setTimeout(() => el.remove(), 5500);
    }, i * 75);
  }
}

const SVG_CORAZON = '<svg viewBox="0 0 24 22" aria-hidden="true"><path d="M12 20.5C5.5 15.6 2 12.2 2 7.9 2 4.8 4.4 2.5 7.3 2.5c1.9 0 3.6 1 4.7 2.6 1.1-1.6 2.8-2.6 4.7-2.6 2.9 0 5.3 2.3 5.3 5.4 0 4.3-3.5 7.7-10 12.6z"/></svg>';
/* ============================================================
   CORAZONES DEL DÍA Y RECUERDOS PIXEL
   - Corazones: 10 por día. Se llenan con "Regálame una sonrisa" o abriendo una carta "Ábreme cuando".
     Cada día empiezan de nuevo.
   - Recuerdos pixel: cada 5 veces que toca "Regálame una sonrisa" (en total) se desbloquea uno.
     Si `imagen` está vacía, sale como "lo estoy dibujando".
   ============================================================ */
const CORAZONES_POR_DIA = 10;
const SONRISAS_POR_RECUERDO = 5;
const HITOS_PIXEL = [
  { titulo: 'Nuestro primer cumplemes', imagen: 'assets/pixel/lluvia.gif', frase: 'Recuerdo de cómo corrimos bajo la lluvia en nuestro primer cumplemes.' },
  { titulo: 'Nuestro almuerzo de nuestro cumplemes', imagen: 'assets/pixel/cena.gif', frase: 'El Eduardo se llenó con las papas y no pudo comer más carne :(' },
  { titulo: 'Nuestra tarde en la laguna', imagen: 'assets/pixel/laguna.gif', frase: '' },
  { titulo: 'Dormiditos abrazados', imagen: 'assets/pixel/dormir.gif', frase: 'Tuvimos que dormir porque el Eduardo estaba muy cansadito por sus vecinos JSJSJS' },
  { titulo: 'Estudiando juntos', imagen: 'assets/pixel/estudio.gif', frase: 'Dallana tratando de explicarme la materia y no estoy entendiendo nada' }
].map((h, i) => ({ ...h, sonrisas: (i + 1) * SONRISAS_POR_RECUERDO }));
const txtSonrisas = n => n === 1 ? '1 sonrisa' : `${n} sonrisas`;
const hoyLocal = () => new Date().toLocaleDateString('en-CA');

let sonrisas = 0;
try { sonrisas = Math.max(0, parseInt(localStorage.getItem('dallanaSonrisas') || '0', 10) || 0); } catch {}

function leerCorazonesHoy() {
  const d = leerJSON('dallanaCorazonesHoy', {});
  return d.fecha === hoyLocal() ? Math.min(CORAZONES_POR_DIA, d.n || 0) : 0;
}

/* Días que entra: solo para avisarte por ntfy */
let diasVisitados = leerSet('dallanaDias');
function registrarDia() {
  const hoy = hoyLocal();
  if (diasVisitados.has(hoy)) return;
  diasVisitados.add(hoy);
  guardarSet('dallanaDias', diasVisitados);
  const n = diasVisitados.size;
  notificar(`entró a la página: lleva ${n} ${n === 1 ? 'día' : 'días'} distintos visitándola 💗`, 'calendar');
}

/* Una interacción del día (sonrisa o carta "Ábreme cuando") llena un corazón */
function sumarCorazon() {
  const antes = leerCorazonesHoy();
  if (antes >= CORAZONES_POR_DIA) return;
  const n = antes + 1;
  guardarJSON('dallanaCorazonesHoy', { fecha: hoyLocal(), n });
  actualizarProgreso();
  if (n === CORAZONES_POR_DIA) {
    lanzarCelebracion();
    alejandroReacciona('aplaudir', 3200);
    notificar(`llenó sus ${CORAZONES_POR_DIA} corazones de hoy 💗`, 'sparkling_heart');
  }
}

function sumarSonrisa() {
  sonrisas++;
  try { localStorage.setItem('dallanaSonrisas', String(sonrisas)); } catch {}
  sumarCorazon();
  actualizarProgreso();
  const hito = HITOS_PIXEL.find(h => h.sonrisas === sonrisas);
  if (hito) {
    notificar(`desbloqueó un recuerdo pixel con ${txtSonrisas(sonrisas)}: «${hito.titulo}»`, 'tada');
    setTimeout(() => abrirHitoPixel(hito, true), 1300);
    alejandroReacciona('aplaudir', 2400);
  }
}

function pintarCorazones(llenos, total) {
  const caja = $('progressHearts'); if (!caja) return;
  if (caja.children.length !== total) {
    caja.innerHTML = '';
    for (let i = 0; i < total; i++) {
      const c = document.createElement('span');
      c.className = 'ph-corazon'; c.style.setProperty('--i', i);
      c.innerHTML = SVG_CORAZON;
      caja.append(c);
    }
  }
  [...caja.children].forEach((c, i) => {
    const lleno = i < llenos;
    if (lleno && !c.classList.contains('lleno') && caja.dataset.listo) {
      c.classList.add('late'); setTimeout(() => c.classList.remove('late'), 700);
    }
    c.classList.toggle('lleno', lleno);
  });
  caja.dataset.listo = '1';
  caja.classList.toggle('completo', llenos >= total);
}

function actualizarProgreso() {
  const hoy = leerCorazonesHoy();
  pintarCorazones(hoy, CORAZONES_POR_DIA);
  const caja = $('progressHearts'); if (caja) caja.setAttribute('aria-label', `${hoy} de ${CORAZONES_POR_DIA} corazones de hoy`);
  const label = $('progressLabel');
  if (label) {
    if (hoy === 0) label.textContent = 'Cada sonrisa o carta que abras hoy llena un corazón';
    else if (hoy < CORAZONES_POR_DIA) label.textContent = `Llevas ${hoy} de ${CORAZONES_POR_DIA} corazones hoy`;
    else label.textContent = '¡Llenaste tus corazones de hoy! Mañana se vuelven a llenar ♥';
  }
  const hl = $('hitoLabel');
  if (hl) {
    const proximo = HITOS_PIXEL.find(h => h.sonrisas > sonrisas);
    if (proximo) {
      const f = proximo.sonrisas - sonrisas;
      hl.textContent = `Te ${f === 1 ? 'falta' : 'faltan'} ${txtSonrisas(f)} para el próximo recuerdo pixel`;
    } else hl.textContent = '¡Desbloqueaste todos los recuerdos pixel! ♥';
  }
  pintarHitos();
}

function pintarHitos() {
  const host = $('pixelHitos'); if (!host) return;
  host.innerHTML = '';
  HITOS_PIXEL.forEach((h, i) => {
    const abierto = sonrisas >= h.sonrisas;
    const faltan = h.sonrisas - sonrisas;
    const txtFaltan = `${faltan === 1 ? 'falta' : 'faltan'} ${txtSonrisas(faltan)}`;
    const b = document.createElement('button');
    b.type = 'button';
    b.className = 'pixel-hito' + (abierto ? ' abierto' : '');
    b.innerHTML = `<span class="pixel-hito-icono" aria-hidden="true">${abierto ? (h.imagen ? '▶' : '✏') : '🔒'}</span><span>Recuerdo ${i + 1}</span>`;
    b.setAttribute('aria-label', abierto ? `Ver el recuerdo ${i + 1}: ${h.titulo}` : `Recuerdo ${i + 1} bloqueado: ${txtFaltan}`);
    b.onclick = () => {
      if (!abierto) {
        const hl = $('hitoLabel');
        if (hl) hl.textContent = `El recuerdo ${i + 1} se abre con ${txtSonrisas(h.sonrisas)}: ${txtFaltan} 🔒`;
        return;
      }
      abrirHitoPixel(h);
    };
    host.append(b);
  });
}

function abrirHitoPixel(h, celebrar = false) {
  const dlg = $('pixelDialog'); if (!dlg) return;
  if (dlg.open) dlg.close();
  const t = $('pixelTitulo'); if (t) t.textContent = h.titulo;
  const img = $('pixelImg');
  if (img) { img.hidden = !h.imagen; if (h.imagen) img.src = h.imagen; }
  const frase = $('pixelFrase');
  if (frase) {
    frase.textContent = h.imagen ? (h.frase || '') : 'Este recuerdo lo estoy dibujando para ti. Vuelve pronto ✏️';
    frase.hidden = !frase.textContent;
  }
  if (celebrar) lanzarCelebracion();
  dlg.showModal();
  notificar(`vio el recuerdo pixel «${h.titulo}»`, 'art');
}

/* ============================================================
   MEMORIAS
   ============================================================ */
function urlFoto(foto) {
  if (!foto) return '';
  try { return new URL(foto, `${URL_BACKEND}/`).href; } catch { return foto; }
}

// Corazoncitos que salen del sello cada vez que llega un mensaje nuevo
function soltarCorazoncitos(paper) {
  if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const colores = ['#e0303f', '#3d72c4', '#4f9a4a', '#ff5a5f'];
  for (let i = 0; i < 6; i++) {
    const c = document.createElement('span');
    c.className = 'paper-chispa'; c.textContent = '♥'; c.setAttribute('aria-hidden', 'true');
    c.style.color = colores[i % colores.length];
    c.style.setProperty('--dx', `${Math.round(Math.random() * 70 - 45)}px`);
    c.style.setProperty('--dy', `${Math.round(-40 - Math.random() * 50)}px`);
    c.style.animationDelay = `${i * 70}ms`;
    paper.append(c);
    setTimeout(() => c.remove(), 1500);
  }
}

function mostrar(d, label = 'Un mensaje para ti') {
  if (!d) return;
  currentId = String(d.id);
  currentMensaje = d.mensaje || '';
  const tag = $('tag'); if (tag) tag.textContent = label;
  const msg = $('message'); if (msg) escribirConResaltes(msg, d.mensaje || '');
  const image = $('memory');
  const url = urlFoto(d.foto);
  if (image) {
    image.classList.remove('show');
    const note = $('memoryNote'); if (note) note.classList.remove('show');
    image.removeAttribute('src');
    if (url) {
      image.onload = () => { image.classList.add('show'); if (note) note.classList.add('show'); };
      image.onerror = () => { image.classList.remove('show'); if (note) note.classList.remove('show'); };
      image.src = url;
    }
  }
  if (!esSaludo(currentId)) { seen.add(currentId); guardarSet('dallanaSeen', seen); }
  const fav = $('favorite');
  if (fav) {
    fav.textContent = favorites.has(currentId) ? '♥' : '♡';
    fav.classList.toggle('favorite', favorites.has(currentId));
  }
  const paper = $('paper');
  if (paper) {
    paper.classList.remove('new'); void paper.offsetWidth;
    paper.classList.add('new');
    setTimeout(() => paper.classList.remove('new'), 900);
    soltarCorazoncitos(paper);
  }
}

async function pedir(url, label = 'Un mensaje para ti') {
  const foot = $('foot'); if (foot) foot.textContent = 'Buscando un recuerdo bonito…';
  let wakeTimer = null;
  if (API_DISPONIBLE) {
    wakeTimer = setTimeout(() => {
      if (foot) foot.textContent = 'Despertando nuestro rincón en el servidor... 💌';
    }, 1400);
    try {
      const r = await fetch(url);
      clearTimeout(wakeTimer);
      if (!r.ok) throw new Error();
      const data = await r.json();
      mostrar(data, data.tipo || label);
      if (foot) foot.textContent = `${seen.size} ${seen.size === 1 ? 'recuerdo descubierto' : 'recuerdos descubiertos'} · ${favorites.size} favoritos ♥`;
      return;
    } catch {
      clearTimeout(wakeTimer);
    }
  }
  const opciones = RESPALDO.filter(item => item.id !== currentId);
  const item = opciones[Math.floor(Math.random() * opciones.length)] || RESPALDO[0];
  mostrar(item, label);
  if (foot) foot.textContent = `${seen.size} ${seen.size === 1 ? 'recuerdo descubierto' : 'recuerdos descubiertos'} · ${favorites.size} favoritos ♥`;
}

/* ============================================================
   CARTAS "ÁBREME CUANDO..."
   ============================================================ */
// Como una carta escrita a mano: las primeras palabras de cada frase van resaltadas con marcador
function escribirConResaltes(el, texto) {
  const tonos = ['r', 'a', 'v', 'm'];
  const frases = String(texto).match(/[^.!?]+[.!?]*\s*/g) || [String(texto)];
  el.replaceChildren();
  frases.forEach((f, i) => {
    const m = f.match(/^(\s*)(\S+\s+\S+)([\s\S]*)$/);
    if (!m) { el.append(f); return; }
    const mk = document.createElement('mark');
    mk.className = `resalte resalte--${tonos[i % tonos.length]}`;
    mk.textContent = m[2];
    el.append(m[1], mk, m[3]);
  });
}

/* En teléfono, achica la letra de la nota hasta que quepa entera (sin scroll), para ver texto y decoraciones juntos */
function ajustarNotaAPantalla() {
  const nota = document.querySelector('.animated-note');
  const p = $('openWhenMessage'), h = $('openWhenNoteTitle');
  if (!nota || !p || !h) return;
  p.style.fontSize = ''; h.style.fontSize = '';
  if (innerWidth >= 600) return;
  let size = parseFloat(getComputedStyle(p).fontSize);
  const ratioTitulo = parseFloat(getComputedStyle(h).fontSize) / size;
  while (nota.scrollHeight > nota.clientHeight + 1 && size > 12) {
    size -= 0.5;
    p.style.fontSize = `${size}px`;
    h.style.fontSize = `${size * ratioTitulo}px`;
  }
}
addEventListener('resize', () => { if ($('openWhenDialog')?.open) ajustarNotaAPantalla(); });

function abrirCartaDeAnimo(carta) {
  const scene = $('letterScene');
  const dlg = $('openWhenDialog');
  if (!scene || !dlg) return;
  scene.classList.remove('is-opening', 'is-open');
  const t1 = $('openWhenNoteTitle'); if (t1) t1.textContent = carta.titulo || 'Una carta para ti';
  const m = $('openWhenMessage'); if (m) escribirConResaltes(m, carta.mensaje || 'Aquí tienes unas palabras para este momento.');
  const t2 = $('openWhenDialogTitle'); if (t2) t2.textContent = carta.titulo || 'Una carta para ti';
  dlg.showModal();
  notificar(`abrió la carta «${carta.titulo || 'Ábreme cuando'}»`, 'envelope');
  sumarCorazon();
  ajustarNotaAPantalla();
  if (document.fonts) document.fonts.ready.then(ajustarNotaAPantalla);
  requestAnimationFrame(() => scene.classList.add('is-opening'));
  const delay = matchMedia('(prefers-reduced-motion: reduce)').matches ? 0 : 620;
  setTimeout(() => { if (dlg.open) scene.classList.add('is-open'); }, delay);
}

function renderCartas() {
  const host = $('letterCards'); if (!host) return;
  host.replaceChildren();
  if (!(contenido.cartas || []).length) {
    const empty = document.createElement('div'); empty.className = 'empty-state';
    empty.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 4H12.2l-1.1 3.3c-.4 1.2-1.5 2-2.8 2h0c-1.3 0-2.4-.8-2.8-2L10.2 4H4c-1.1 0-2 .9-2 2v13c0 1.1.9 2 2 2h16a2 2 0 0 0 2-2V6c0-1.1-.9-2-2-2z"/><path d="M19 16V8a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v8"/><path d="M7 4h2"/><path d="M17 4h2"/><path d="M11 19h2"/><path d="M11 7h2"/></svg>';
    empty.innerHTML += '<p>Aún no hay cartas escritas. Pronto llegarán unas palabras para ti.</p>';
    host.append(empty);
    return;
  }
  (contenido.cartas || []).forEach((c, i) => {
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'open-card';
    const titulo = c.titulo || `Carta ${i + 1}`;
    // Sobre: solapa, carta asomando y sello; "Ábreme cuando" va como etiqueta y el resto a mano
    const m = titulo.match(/^(ábreme cuando)\s+(.+)$/i);
    const deco = cls => { const s = document.createElement('span'); s.className = cls; s.setAttribute('aria-hidden', 'true'); return s; };
    const sello = deco('oc-seal'); sello.textContent = '♥';
    const etiqueta = deco('oc-label'); etiqueta.textContent = m ? m[1] : `Carta Nº ${i + 1}`;
    const texto = document.createElement('span'); texto.className = 'oc-title'; texto.textContent = m ? m[2] : titulo;
    b.append(deco('oc-letter'), deco('oc-flap'), deco('oc-cordel'), deco('oc-ramito'), sello, deco('oc-deco oc-deco--i'), deco('oc-deco oc-deco--d'), etiqueta, texto);
    b.setAttribute('aria-label', titulo);
    b.setAttribute('aria-haspopup', 'dialog');
    b.onclick = () => abrirCartaDeAnimo(c);
    host.append(b);
  });
}

/* ============================================================
   MUSEO
   ============================================================ */
function renderMuseo() {
  const host = $('museumGrid'); const section = $('museumSection');
  if (!host || !section) return;
  host.replaceChildren();
  const items = (contenido.museo || []).filter(it => it && it.titulo && (it.descripcion || it.mensaje));
  section.hidden = items.length === 0;
  if (!items.length) {
    const empty = document.createElement('div'); empty.className = 'empty-state';
    empty.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>';
    empty.innerHTML += '<p>El museo está vacío. Pronto se llenará de vitrinas sobre ti.</p>';
    host.append(empty);
    return;
  }
  items.forEach((item, i) => {
    const card = document.createElement('article'); card.className = 'museum-card';
    const icon = document.createElement('span'); icon.className = 'museum-icon';
    icon.setAttribute('aria-hidden', 'true'); icon.textContent = ['✿', '♡', '✧', '☼'][i % 4];
    const title = document.createElement('h3'); title.textContent = item.titulo;
    const desc = document.createElement('p'); desc.textContent = item.descripcion || item.mensaje;
    card.append(icon, title, desc);
    if (item.descripcion && item.mensaje) { const s = document.createElement('small'); s.textContent = item.mensaje; card.append(s); }
    host.append(card);
  });
}

function renderFrasco() {
  const host = $('frascoNotes'); if (!host) return;
  host.replaceChildren();
  if (!(contenido.frasco || []).length) {
    const empty = document.createElement('div'); empty.className = 'empty-state';
    empty.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/><path d="M12 17v4"/><path d="M8 21h8"/></svg>';
    empty.innerHTML += '<p>El frasco está vacío. Pronto aparecerán notas sorpresa aquí.</p>';
    host.append(empty);
    return;
  }
  (contenido.frasco || []).forEach((nota, i) => {
    const el = document.createElement('div');
    el.className = 'jar-note';
    el.textContent = nota;
    el.style.setProperty('--i', String(i));
    host.append(el);
  });
}

function renderSuenos() {
  const host = $('suenosList'); if (!host) return;
  host.replaceChildren();
  const done = leerSet('dallanaDreamsDone');
  if (!(contenido.suenos || []).length) {
    const empty = document.createElement('div'); empty.className = 'empty-state';
    empty.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h9l-1 8 10-12h-9l-1-8z"/><path d="M13 18H6"/><path d="M17 12H7"/></svg>';
    empty.innerHTML += '<p>No hay aventuras registradas todavía. Pronto llenarás esta lista.</p>';
    host.append(empty);
    return;
  }
  (contenido.suenos || []).forEach((s, i) => {
    const el = document.createElement('div');
    el.className = 'sueno-item' + (done.has(s.id || String(i)) ? ' done' : '');
    const t = document.createElement('h3'); t.textContent = s.titulo || `Sueño ${i + 1}`;
    const m = document.createElement('p'); m.textContent = s.descripcion || '';
    el.append(t, m);
    el.onclick = () => {
      const id = s.id || String(i);
      if (done.has(id)) { done.delete(id); el.classList.remove('done'); }
      else { done.add(id); el.classList.add('done'); }
      guardarSet('dallanaDreamsDone', done);
    };
    host.append(el);
  });
}

function renderAutoestima() {
  const host = $('autoestimaList'); if (!host) return;
  host.replaceChildren();
  if (!(contenido.autoestima || []).length) {
    const empty = document.createElement('div'); empty.className = 'empty-state';
    empty.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><circle cx="12" cy="8" r="7"/></svg>';
    empty.innerHTML += '<p>Aquí aparecerán recordatorios bonitos sobre ti.</p>';
    host.append(empty);
    return;
  }
  (contenido.autoestima || []).forEach((item, i) => {
    const el = document.createElement('div');
    el.className = 'affirmation-card';
    const texto = typeof item === 'string' ? item : item.texto || '';
    el.textContent = texto;
    host.append(el);
  });
}

/* ============================================================
   RENDER GLOBAL
   ============================================================ */
function renderContenido() { renderCartas(); renderMuseo(); renderFrasco(); renderSuenos(); renderAutoestima(); }

// Reemplaza el contenido local por el que se editó en el panel (si la API responde).
async function cargarContenido() {
  if (!API_DISPONIBLE) return;
  try {
    const r = await fetch(`${URL_BACKEND}/api/contenido`);
    if (!r.ok) return;
    const d = await r.json();
    const c = d.contenido || d;
    const local = CONTENIDO_LOCAL;
    contenido = {
      autoestima: Array.isArray(c.autoestima) && c.autoestima.length ? c.autoestima : local.autoestima,
      cartas: Array.isArray(c.cartas) && c.cartas.length ? c.cartas : local.cartas,
      frasco: Array.isArray(c.frasco) && c.frasco.length ? c.frasco : local.frasco,
      museo: Array.isArray(c.museo) ? c.museo : local.museo,
      suenos: Array.isArray(c.suenos) ? c.suenos : local.suenos
    };
    renderContenido();
  } catch {}
}

/* ============================================================
   CARTA FINAL
   ============================================================ */
// Divide la carta en saludo, subtítulo, cuerpo y firma para darle formato.
function mostrarCarta(texto) {
  const destino = $('letterText'); if (!destino) return;
  const partes = String(texto || '').split(/\n\s*\n/).map(t => t.trim()).filter(Boolean);
  let finFirma = partes.length;
  while (finFirma > 2 && partes.length - finFirma < 2 && partes[finFirma - 1].length <= 30) finFirma--;
  let primerCuerpo = true;
  destino.replaceChildren(...partes.map((t, i) => {
    let el;
    if (i === 0 && t.length <= 60) { el = document.createElement('h3'); el.className = 'letter-greeting'; }
    else if (i === 1 && t.length <= 60 && partes.length > 3) { el = document.createElement('p'); el.className = 'letter-subtitle'; }
    else if (i >= finFirma) { el = document.createElement('p'); el.className = 'letter-sign'; }
    else { el = document.createElement('p'); if (primerCuerpo) { el.className = 'letter-first'; primerCuerpo = false; } }
    el.textContent = t;
    return el;
  }));
}

// La carta local es la versión completa. Solo se reemplaza si en el servidor
// hay una carta escrita desde el panel (el backend devuelve '' por defecto).
async function cargarCarta() {
  mostrarCarta(CARTA_LOCAL);
  if (!API_DISPONIBLE) return;
  try {
    const r = await fetch(`${URL_BACKEND}/api/carta`);
    if (!r.ok) return;
    const d = await r.json();
    if (typeof d.carta === 'string' && d.carta.trim()) mostrarCarta(d.carta);
  } catch {}
}

/* ============================================================
   ENVELOPE / RANDOM / DAILY / FAVORITE
   ============================================================ */
const openEnvelopeBtn = $('openEnvelope');
if (openEnvelopeBtn) openEnvelopeBtn.onclick = () => {
  const cover = $('welcome');
  const env = $('env');
  if (cover && cover.classList.contains('opening')) return;
  if (cover) cover.classList.add('opening');
  notificar('abrió el sobre de la portada', 'envelope_with_arrow');
  if (env) env.classList.add('open');
  const delay = matchMedia('(prefers-reduced-motion: reduce)').matches ? 0 : 780;
  setTimeout(() => {
    if (cover) { cover.classList.add('closed'); cover.classList.remove('opening'); }
    pedir(`${URL_BACKEND}/api/momento`, 'Un mensaje para ti');
    saludoAlejandro();
  }, delay);
};

const randomBtn = $('random');
if (randomBtn) randomBtn.onclick = () => {
  vibrar();
  actividad.recuerdos++;
  sumarSonrisa();
  const q = currentId ? `?ultimo=${encodeURIComponent(currentId)}` : '';
  pedir(`${URL_BACKEND}/api/cumplido${q}`);
};

const dailyBtn = $('daily');
if (dailyBtn) dailyBtn.onclick = () => {
  vibrar();
  notificar('vio el mensaje del día', 'sunny');
  if (API_DISPONIBLE) { pedir(`${URL_BACKEND}/api/del-dia`, 'Tu mensaje de hoy'); return; }
  const ahora = new Date();
  const n = Math.floor(Date.UTC(ahora.getFullYear(), ahora.getMonth(), ahora.getDate()) / 864e5);
  const item = RESPALDO[((n % RESPALDO.length) + RESPALDO.length) % RESPALDO.length];
  mostrar(item, 'Tu mensaje de hoy');
  const foot = $('foot');
  if (foot) foot.textContent = `${seen.size} ${seen.size === 1 ? 'recuerdo descubierto' : 'recuerdos descubiertos'} · ${favorites.size} favoritos ♥`;
};

const favBtn = $('favorite');
if (favBtn) favBtn.onclick = () => {
  if (!currentId) return;
  if (favorites.has(currentId)) {
    favorites.delete(currentId);
    delete favoriteTexts[currentId];
  } else {
    favorites.add(currentId);
    favoriteTexts[currentId] = currentMensaje;
    notificar(`guardó un favorito: «${String(currentMensaje || '').slice(0, 120)}»`, 'star');
  }
  guardarSet('dallanaFavorites', favorites);
  guardarJSON('dallanaFavoriteTexts', favoriteTexts);
  favBtn.textContent = favorites.has(currentId) ? '♥' : '♡';
  favBtn.classList.toggle('favorite', favorites.has(currentId));
  actualizarBotonFavoritos();
  const foot = $('foot');
  if (foot) foot.textContent = favorites.has(currentId) ? 'Guardado entre tus favoritos ♥' : 'Quitado de tus favoritos';
};

/* ============================================================
   FAVORITOS
   ============================================================ */
function actualizarBotonFavoritos() {
  const count = $('favCount');
  if (count) count.textContent = String(favorites.size);
}

function encontrarMensajePorId(id) {
  const clave = String(id);
  if (favoriteTexts[clave]) return { id: clave, mensaje: favoriteTexts[clave], foto: '' };
  const item = mensajes.find(m => String(m.id) === clave) || RESPALDO.find(m => m.id === clave);
  return item || { id: clave, mensaje: 'Un recuerdo guardado con amor ♥' };
}

function renderFavoritos() {
  const host = $('favoritesList');
  if (!host) return;
  host.replaceChildren();
  if (favorites.size === 0) {
    const p = document.createElement('p');
    p.className = 'favorite-empty';
    p.textContent = 'Aún no has guardado recuerdos favoritos. Toca el corazón ♡ en cualquier recuerdo para guardarlo aquí.';
    host.append(p);
    return;
  }
  favorites.forEach(id => {
    const item = encontrarMensajePorId(id);
    const card = document.createElement('article');
    card.className = 'favorite-item';
    const text = document.createElement('p');
    text.textContent = item.mensaje || '';
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'icon-btn';
    btn.textContent = '✕';
    btn.title = 'Quitar de favoritos';
    btn.setAttribute('aria-label', 'Quitar de favoritos');
    btn.onclick = (e) => {
      e.stopPropagation();
      favorites.delete(String(id));
      delete favoriteTexts[String(id)];
      guardarSet('dallanaFavorites', favorites);
      guardarJSON('dallanaFavoriteTexts', favoriteTexts);
      actualizarBotonFavoritos();
      const fav = $('favorite');
      if (fav && currentId === String(id)) {
        fav.textContent = '♡';
        fav.classList.remove('favorite');
      }
      renderFavoritos();
    };
    card.onclick = () => {
      mostrar(item, 'Un recuerdo favorito');
      const dlg = $('favoritesDialog');
      if (dlg) dlg.close();
      const paper = $('paper');
      if (paper) paper.scrollIntoView({ behavior: 'smooth', block: 'center' });
    };
    card.style.cursor = 'pointer';
    card.append(text, btn);
    host.append(card);
  });
}

const viewFavoritesBtn = $('viewFavorites');
if (viewFavoritesBtn) viewFavoritesBtn.onclick = () => {
  renderFavoritos();
  const dlg = $('favoritesDialog');
  if (dlg) dlg.showModal();
};

const openLetterBtn = $('openLetter');
if (openLetterBtn) openLetterBtn.onclick = () => {
  lanzarCelebracion();
  cargarCarta();
  const dlg = $('letterDialog'); if (dlg) dlg.showModal();
  notificar('abrió tu carta principal 💌', 'love_letter');
};


const resetBtn = $('resetProgress');
if (resetBtn) resetBtn.onclick = () => {
  if (!confirm('¿Quieres reiniciar tu progreso en este rincón?')) return;
  ['dallanaSeen', 'dallanaFavorites', 'dallanaFavoriteTexts', 'dallanaDreamsDone', 'dallanaLetterUnlocked', 'dallanaSonrisas', 'dallanaCorazonesHoy'].forEach(k => { try { localStorage.removeItem(k); } catch {} });
  seen = new Set(); favorites = new Set(); favoriteTexts = {};
  actualizarBotonFavoritos();
  location.reload();
};

document.querySelectorAll('[data-close]').forEach(b => b.onclick = () => {
  const el = $(b.dataset.close); if (el) el.close();
});

const openWhenDlg = $('openWhenDialog');
if (openWhenDlg) openWhenDlg.addEventListener('close', () => {
  const scene = $('letterScene'); if (scene) scene.classList.remove('is-opening', 'is-open');
});

/* ============================================================
   MÚSICA
   ============================================================ */
let musicIndex = 0;
const musicAudio = $('musicAudio');
const ICONO_PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13L19 12z"/></svg>';
const ICONO_PAUSA = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14M16 5v14"/></svg>';
const musicWave = $('musicWave');
const WAVE_BARRAS = 40;

if (musicWave) {
  for (let i = 0; i < WAVE_BARRAS; i++) {
    const alto = 30 + Math.round(55 * Math.abs(Math.sin(i * 0.55) * Math.cos(i * 0.21)) + (i * 37 % 15));
    const barra = document.createElement('i');
    barra.className = 'wave-bar';
    barra.style.setProperty('--height', `${alto}%`);
    musicWave.appendChild(barra);
  }
}

function formatoTiempo(seg) {
  if (!Number.isFinite(seg) || seg < 0) return '0:00';
  const total = Math.floor(seg);
  return `${Math.floor(total / 60)}:${String(total % 60).padStart(2, '0')}`;
}

function pintarProgreso() {
  if (!musicWave || !musicAudio) return;
  const dur = musicAudio.duration;
  const frac = Number.isFinite(dur) && dur > 0 ? Math.min(1, musicAudio.currentTime / dur) : 0;
  const encendidas = Math.round(frac * WAVE_BARRAS);
  musicWave.querySelectorAll('.wave-bar').forEach((barra, i) => barra.classList.toggle('on', i < encendidas));
  musicWave.setAttribute('aria-valuenow', String(Math.round(frac * 100)));
  const cur = $('musicCur'); if (cur) cur.textContent = formatoTiempo(musicAudio.currentTime);
  const total = $('musicDur'); if (total) total.textContent = formatoTiempo(dur);
}

function buscarEnPista(frac) {
  if (!musicAudio || !Number.isFinite(musicAudio.duration)) return;
  musicAudio.currentTime = Math.max(0, Math.min(1, frac)) * musicAudio.duration;
  pintarProgreso();
}

function actualizarPista(indice, reproducir = false) {
  musicIndex = (indice + PLAYLIST.length) % PLAYLIST.length;
  const pista = PLAYLIST[musicIndex];
  const h = document.querySelector('.track-heading h2'); if (h) h.textContent = pista.nombre;
  const p = document.querySelector('.track-heading p'); if (p) p.textContent = `Canción ${musicIndex + 1} de ${PLAYLIST.length}`;
  if (!musicAudio) return;
  musicAudio.src = `assets/musica/${encodeURIComponent(pista.archivo)}`;
  pintarProgreso();
  if (reproducir) musicAudio.play().then(() => {
    const hint = $('musicHint'); if (hint) hint.textContent = `Reproduciendo: ${pista.nombre}`;
  }).catch(() => {
    const hint = $('musicHint'); if (hint) hint.textContent = 'No se pudo reproducir esta canción.';
  });
}

// Deja la primera pista lista antes de que se pulse reproducir. Así el gesto del
// usuario no compite con un cambio de fuente que algunos navegadores cancelan.
actualizarPista(musicIndex);

const musicPrev = $('musicPrev');
if (musicPrev) musicPrev.onclick = () => actualizarPista(musicIndex - 1, Boolean(musicAudio && !musicAudio.paused));

const musicNext = $('musicNext');
if (musicNext) musicNext.onclick = () => actualizarPista(musicIndex + 1, Boolean(musicAudio && !musicAudio.paused));

const musicVolume = $('musicVolume');
if (musicVolume) musicVolume.oninput = () => {
  const valor = Number(musicVolume.value);
  const out = $('musicVolumeValue'); if (out) out.value = `${Math.round(valor * 100)}%`;
  if (musicAudio) musicAudio.volume = valor;
};

const musicPlay = $('musicPlay');
if (musicPlay) musicPlay.onclick = async () => {
  if (!musicAudio) return;
  if (!musicAudio.paused) {
    musicAudio.pause();
    musicPlay.closest('.music-player')?.classList.remove('is-playing');
    musicPlay.innerHTML = ICONO_PLAY;
    musicPlay.setAttribute('aria-label', 'Reproducir música');
    musicPlay.setAttribute('aria-pressed', 'false');
    const hint = $('musicHint'); if (hint) hint.textContent = 'Melodía en pausa';
    return;
  }
  if (!musicAudio.src) actualizarPista(musicIndex);
  musicAudio.volume = Number(musicVolume ? musicVolume.value : 0.35);
  try { await musicAudio.play(); } catch {
    const hint = $('musicHint'); if (hint) hint.textContent = 'No se pudo iniciar la reproducción.';
    return;
  }
  musicPlay.closest('.music-player')?.classList.add('is-playing');
  musicPlay.innerHTML = ICONO_PAUSA;
  musicPlay.setAttribute('aria-label', 'Pausar música');
  musicPlay.setAttribute('aria-pressed', 'true');
  const hint = $('musicHint'); if (hint) hint.textContent = `Reproduciendo: ${PLAYLIST[musicIndex].nombre}`;
};

if (musicAudio) {
  musicAudio.onended = () => actualizarPista(musicIndex + 1, true);
  musicAudio.onerror = () => {
    const hint = $('musicHint'); if (hint) hint.textContent = 'No se pudo cargar esta canción.';
  };
  musicAudio.ontimeupdate = pintarProgreso;
  musicAudio.onloadedmetadata = pintarProgreso;
}

if (musicWave) {
  musicWave.onclick = (e) => {
    const r = musicWave.getBoundingClientRect();
    buscarEnPista((e.clientX - r.left) / r.width);
  };
  musicWave.onkeydown = (e) => {
    if (!musicAudio || !Number.isFinite(musicAudio.duration)) return;
    if (e.key === 'ArrowRight') { musicAudio.currentTime = Math.min(musicAudio.duration, musicAudio.currentTime + 5); e.preventDefault(); }
    if (e.key === 'ArrowLeft') { musicAudio.currentTime = Math.max(0, musicAudio.currentTime - 5); e.preventDefault(); }
    pintarProgreso();
  };
}

/* ============================================================
   CORAZÓN SECRETO
   ============================================================ */
const secretHeart = $('secretHeart');
if (secretHeart) secretHeart.onclick = () => {
  toquesSecretos++;
  if (toquesSecretos >= 5) {
    const sm = $('secretMessage'); if (sm) sm.hidden = false;
    const aa = $('albumArt'); if (aa) aa.classList.add('secret-found');
    const hint = $('musicHint'); if (hint) hint.textContent = 'Encontraste un detalle escondido.';
    toquesSecretos = 0;
  }
};

/* ============================================================
   ADMIN
   ============================================================ */
function estadoAdmin(texto, error = false) {
  const el = $('adminStatus'); if (!el) return;
  el.textContent = texto;
  el.classList.toggle('error', error);
}

async function adminFetch(path, options = {}) {
  if (!API_DISPONIBLE) throw new Error('El panel privado necesita que primero conectes y despliegues la API en Render.');
  const headers = { 'X-Admin-Token': token, ...options.headers };
  if (!(options.body instanceof FormData)) headers['Content-Type'] = 'application/json';
  return fetch(`${URL_BACKEND}${path}`, { ...options, headers });
}

// FastAPI devuelve `detail` como texto o como lista de errores de validación.
async function errorDeApi(r, fallback) {
  try {
    const { detail } = await r.json();
    if (typeof detail === 'string') return new Error(detail);
    if (Array.isArray(detail) && detail.length) return new Error(detail.map(d => d.msg || String(d)).join(' · '));
  } catch {}
  return new Error(`${fallback} (error ${r.status}).`);
}

function seleccionarMensaje() {
  const id = $('editSelect')?.value;
  const item = mensajes.find(m => String(m.id) === id);
  if (!item) return;
  $('editMessage').value = item.mensaje;
  $('editPhoto').value = item.foto || '';
  $('editPhotoFile').value = '';
}

function renderMensajes() {
  const select = $('editSelect'); if (!select) return;
  select.replaceChildren();
  mensajes.forEach((m, i) => {
    const option = document.createElement('option');
    option.value = String(m.id);
    option.textContent = `${i + 1}. ${m.mensaje.slice(0, 68)}`;
    select.append(option);
  });
  if (mensajes.length) seleccionarMensaje();
}

function previewContenido() {
  try {
    const data = {
      autoestima: JSON.parse($('adminAffirmations').value || '[]'),
      cartas: JSON.parse($('adminCards').value || '[]'),
      frasco: JSON.parse($('adminJar').value || '[]'),
      museo: JSON.parse($('adminMuseum').value || '[]'),
      suenos: JSON.parse($('adminDreams').value || '[]')
    };
    if (!Object.values(data).every(Array.isArray)) throw new Error();
    for (const item of data.cartas) {
      if (!item || typeof item.titulo !== 'string' || typeof item.mensaje !== 'string') throw new Error('Cada carta necesita título y mensaje.');
    }
    for (const item of data.museo) {
      if (!item || typeof item.titulo !== 'string') throw new Error('Cada vitrina del museo necesita título.');
    }
    const prev = $('contentPreview');
    if (prev) prev.textContent = `${data.autoestima.length} autoestima · ${data.cartas.length} cartas · ${data.frasco.length} frasco · ${data.museo.length} museo · ${data.suenos.length} sueños`;
    return data;
  } catch {
    const prev = $('contentPreview');
    if (prev) prev.textContent = 'Revisa el JSON de cada colección antes de guardar.';
    return null;
  }
}

async function entradaAdmin() {
  token = $('adminToken').value;
  try {
    const r = await adminFetch('/api/administracion');
    if (!r.ok) throw await errorDeApi(r, 'No pude validar la clave');
    const d = await r.json();
    mensajes = Array.isArray(d.cumplidos) ? d.cumplidos : [];
    // Si aún no se ha escrito una carta en el servidor, se parte de la carta local completa.
    $('adminLetter').value = d.carta || CARTA_LOCAL;
    $('greetingMorning').value = d.saludos?.manana || '';
    $('greetingNight').value = d.saludos?.noche || '';
    contenidoServidor = d.contenido || null;
    const c = contenidoServidor || contenido;
    const setVal = (id, v) => { const el = $(id); if (el) el.value = v; };
    setVal('adminAffirmations', JSON.stringify(c.autoestima || [], null, 2));
    setVal('adminCards', JSON.stringify(c.cartas || [], null, 2));
    setVal('adminJar', JSON.stringify(c.frasco || [], null, 2));
    setVal('adminMuseum', JSON.stringify(c.museo || [], null, 2));
    setVal('adminDreams', JSON.stringify(c.suenos || [], null, 2));
    previewContenido();
    $('adminTools').classList.remove('hidden');
    renderMensajes();
    estadoAdmin(`Panel listo · ${mensajes.length} recuerdos guardados.`);
  } catch (e) { estadoAdmin(e.message, true); }
}

async function subirFoto(fileInput, destination) {
  const file = fileInput.files?.[0];
  if (!file) return;
  try {
    const body = new FormData();
    body.append('foto', file);
    const r = await adminFetch('/api/administracion/fotos', { method: 'POST', body });
    if (!r.ok) throw await errorDeApi(r, 'No pude subir la imagen');
    const d = await r.json();
    $(destination).value = `${URL_BACKEND}${d.foto}`;
    estadoAdmin('Foto subida. Guarda el recuerdo para aplicar el cambio.');
  } catch (e) { estadoAdmin(e.message, true); }
}

const adminLoginForm = $('adminLoginForm');
if (adminLoginForm) adminLoginForm.onsubmit = e => { e.preventDefault(); entradaAdmin(); };

const editSelect = $('editSelect');
if (editSelect) editSelect.onchange = seleccionarMensaje;

['adminAffirmations', 'adminCards', 'adminJar', 'adminMuseum', 'adminDreams'].forEach(id => {
  const el = $(id); if (el) el.oninput = previewContenido;
});

const adminOpenBtn = $('adminOpen');
if (adminOpenBtn) adminOpenBtn.onclick = () => {
  const dlg = $('adminDialog'); if (!dlg) return;
  dlg.showModal();
  const t = $('adminToken'); if (t) t.value = token;
};

const newPhotoFile = $('newPhotoFile');
if (newPhotoFile) newPhotoFile.onchange = () => subirFoto(newPhotoFile, 'newPhoto');

const editPhotoFile = $('editPhotoFile');
if (editPhotoFile) editPhotoFile.onchange = () => subirFoto(editPhotoFile, 'editPhoto');

const saveEdit = $('saveEdit');
if (saveEdit) saveEdit.onclick = async () => {
  const id = $('editSelect')?.value;
  if (!id) return;
  try {
    const r = await adminFetch(`/api/administracion/cumplidos/${encodeURIComponent(id)}`, {
      method: 'PUT', body: JSON.stringify({ mensaje: $('editMessage').value.trim(), foto: $('editPhoto').value.trim() })
    });
    if (!r.ok) throw await errorDeApi(r, 'No pude guardar el recuerdo');
    const actualizado = await r.json();
    mensajes = mensajes.map(m => String(m.id) === String(actualizado.id) ? actualizado : m);
    renderMensajes(); estadoAdmin('Recuerdo actualizado.');
  } catch (e) { estadoAdmin(e.message, true); }
};

const deleteMessage = $('deleteMessage');
if (deleteMessage) deleteMessage.onclick = async () => {
  const id = $('editSelect')?.value;
  if (!id) return;
  try {
    const r = await adminFetch(`/api/administracion/cumplidos/${encodeURIComponent(id)}`, { method: 'DELETE' });
    if (!r.ok) throw await errorDeApi(r, 'No pude eliminar el recuerdo');
    mensajes = mensajes.filter(m => String(m.id) !== String(id));
    renderMensajes(); estadoAdmin('Recuerdo eliminado.');
  } catch (e) { estadoAdmin(e.message, true); }
};

const addMessage = $('addMessage');
if (addMessage) addMessage.onclick = async () => {
  const mensaje = $('newMessage').value.trim();
  if (!mensaje) return estadoAdmin('Escribe un mensaje antes de guardarlo.', true);
  try {
    const r = await adminFetch('/api/administracion/cumplidos', {
      method: 'POST', body: JSON.stringify({ mensaje, foto: $('newPhoto').value.trim() })
    });
    if (!r.ok) throw await errorDeApi(r, 'No pude añadir el recuerdo');
    $('newMessage').value = ''; $('newPhoto').value = ''; $('newPhotoFile').value = '';
    await entradaAdmin(); estadoAdmin('Nuevo recuerdo añadido.');
  } catch (e) { estadoAdmin(e.message, true); }
};

const saveLetter = $('saveLetter');
if (saveLetter) saveLetter.onclick = async () => {
  try {
    const r = await adminFetch('/api/administracion/carta', { method: 'PUT', body: JSON.stringify({ carta: $('adminLetter').value }) });
    if (!r.ok) throw await errorDeApi(r, 'No pude guardar la carta');
    estadoAdmin('Carta guardada.');
  } catch (e) { estadoAdmin(e.message, true); }
};

const saveGreetings = $('saveGreetings');
if (saveGreetings) saveGreetings.onclick = async () => {
  try {
    const r = await adminFetch('/api/administracion/saludos', {
      method: 'PUT', body: JSON.stringify({ manana: $('greetingMorning').value, noche: $('greetingNight').value })
    });
    if (!r.ok) throw await errorDeApi(r, 'No pude guardar los saludos');
    estadoAdmin('Saludos guardados.');
  } catch (e) { estadoAdmin(e.message, true); }
};

const saveContent = $('saveContent');
if (saveContent) saveContent.onclick = async () => {
  const data = previewContenido();
  if (!data) return estadoAdmin('Revisa el JSON antes de guardar.', true);
  if (!contenidoServidor) return estadoAdmin('Vuelve a entrar al panel antes de guardar.', true);
  try {
    // El backend exige todas las colecciones: se reenvían las que esta página no edita.
    const body = { ...contenidoServidor, ...data };
    const r = await adminFetch('/api/administracion/contenido', { method: 'PUT', body: JSON.stringify(body) });
    if (!r.ok) throw await errorDeApi(r, 'No pude guardar el contenido');
    contenidoServidor = body;
    contenido = data;
    renderContenido();
    estadoAdmin('Contenido guardado.');
  } catch (e) { estadoAdmin(e.message, true); }
};

/* ============================================================
   AVISO DE VISITA
   Enlace para Dallana: Dallana.html?de=dallana
   Para no avisarte a ti mismo, abre una vez Dallana.html?yo=1 en tu navegador.
   ============================================================ */
let avisosActivos = false;
let quienVisita = '';
const actividad = { recuerdos: 0, ultimaCancion: '' };

function notificar(texto, tags = 'heart', titulo = 'Actividad en tu pagina') {
  try {
    if (!avisosActivos) return;
    fetch(`https://ntfy.sh/${NTFY_TEMA}`, {
      method: 'POST',
      body: `${quienVisita} ${texto}`,
      headers: { Title: titulo, Tags: tags },
      keepalive: true
    }).catch(() => {});
  } catch {}
}

function avisarVisita() {
  try {
    if (!NTFY_TEMA) return;
    if (['localhost', '127.0.0.1', ''].includes(location.hostname)) return;
    const params = new URLSearchParams(location.search);
    if (params.get('yo') === '1') { localStorage.setItem('dallanaYo', '1'); return; }
    if (localStorage.getItem('dallanaYo') === '1') return;
    const de = (params.get('de') || '').toLowerCase().replace(/[^a-z0-9_-]/g, '').slice(0, 20);
    quienVisita = de ? de.charAt(0).toUpperCase() + de.slice(1) : 'Alguien (visita anónima)';
    avisosActivos = true;
    if (sessionStorage.getItem('dallanaAvisado')) return;
    sessionStorage.setItem('dallanaAvisado', '1');
    const hora = new Date().toLocaleString('es-CL', { dateStyle: 'short', timeStyle: 'short' });
    notificar(`abrió la página · ${hora}`, de ? 'heart' : 'eyes', 'Visita en tu pagina');
  } catch {}
}

/* Canciones: avisa una vez por canción distinta (no al pausar y reanudar) */
if (musicAudio) musicAudio.addEventListener('play', () => {
  const nombre = PLAYLIST[musicIndex]?.nombre || 'una canción';
  if (nombre === actividad.ultimaCancion) return;
  actividad.ultimaCancion = nombre;
  notificar(`puso «${nombre}»`, 'notes');
});

/* Tiempo en la página: cuenta solo el tiempo con la página a la vista (no el que pasa en otra app)
   y avisa al salir o cambiar de app con lo que duró ese rato y el total de la visita. */
let visibleDesde = document.visibilityState === 'visible' ? Date.now() : 0;
let tiempoTotal = 0;
const formatoDuracion = ms => {
  const seg = Math.round(ms / 1000);
  if (seg < 60) return `${seg} s`;
  const min = Math.floor(seg / 60), resto = seg % 60;
  if (min < 60) return resto ? `${min} min ${resto} s` : `${min} min`;
  return `${Math.floor(min / 60)} h ${min % 60} min`;
};
function cerrarTramo() {
  if (!visibleDesde) return;
  const tramo = Date.now() - visibleDesde;
  visibleDesde = 0;
  tiempoTotal += tramo;
  if (tramo < 10000) return;
  const rec = actividad.recuerdos ? ` · vio ${actividad.recuerdos} ${actividad.recuerdos === 1 ? 'recuerdo' : 'recuerdos'}` : '';
  const total = tiempoTotal > tramo ? ` (total de la visita: ${formatoDuracion(tiempoTotal)})` : '';
  notificar(`estuvo ${formatoDuracion(tramo)} en la página${total}${rec}`, 'hourglass', 'Salio de tu pagina');
}
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'hidden') cerrarTramo();
  else if (!visibleDesde) {
    visibleDesde = Date.now();
    if (tiempoTotal >= 10000) notificar('volvió a la página', 'eyes');
  }
});
addEventListener('pagehide', cerrarTramo);

/* ============================================================
   ALEJANDRO: AYUDANTE QUE CUENTA LAS NOVEDADES
   Para anunciar algo nuevo: cambia NOVEDADES.version y escribe los mensajes.
   Se abre solo una vez por versión; después se puede tocar a Alejandro para volver a verlas.
   ============================================================ */
const NOVEDADES = {
  version: '2026-11-19b',
  mensajes: [
    '¡Hola, Dallana! Me llamo Alejandro y te voy a mostrar las novedades de este espacio. 🦀',
    'Ahora tienes 10 corazones cada día. Se llenan cuando tocas «Regálame una sonrisa» o abres una carta «Ábreme cuando».',
    'Cada 5 sonrisas se desbloquea un recuerdo pixel de ustedes dos. ¡El primero es de su primer cumplemes!',
    'La carta principal ya la puedes leer cuando quieras, en el capítulo 07. 💌',
    'Y hay una canción nueva en la lista: «Those Eyes» de New West. 🎶',
    '¡Y ahora tengo más vida! Aplaudo cuando llenas tus 10 corazones y bailo cuando pones música. 🎶',
    'De noche me duermo 😴, en la mañana bostezo y de vez en cuando salgo a pasear por la pantalla.',
    'Ah… y tengo un secreto. Mantenme presionado un ratito para descubrirlo. 🤫',
    '¡Eso es todo por ahora! Tócame cuando quieras volver a verlas.'
  ]
};
let alejandroPaso = 0;

let alejandroSecreto = false;

function pintarAlejandro() {
  const texto = $('alejandroTexto'), paso = $('alejandroPaso'), sig = $('alejandroSiguiente');
  const total = NOVEDADES.mensajes.length;
  alejandroSecreto = false;
  if (sig) sig.hidden = false;
  if (texto) texto.textContent = NOVEDADES.mensajes[alejandroPaso];
  if (paso) paso.textContent = `${alejandroPaso + 1} de ${total}`;
  if (sig) sig.textContent = alejandroPaso === total - 1 ? '¡Listo!' : 'Siguiente ›';
}

function abrirAlejandro(desde = 0) {
  const globo = $('alejandroGlobo'); if (!globo) return;
  alejandroPaso = desde;
  pintarAlejandro();
  globo.hidden = false;
  $('alejandroSprite')?.setAttribute('aria-expanded', 'true');
  estadoAlejandro();
}

function cerrarAlejandro(leido) {
  const globo = $('alejandroGlobo'); if (!globo) return;
  globo.hidden = true;
  $('alejandroSprite')?.setAttribute('aria-expanded', 'false');
  estadoAlejandro();
  if (alejandroSecreto) { alejandroSecreto = false; return; }
  try { localStorage.setItem('dallanaNovedades', NOVEDADES.version); } catch {}
  if (leido) notificar('leyó las novedades de Alejandro 🦀', 'crab');
}

function saludoAlejandro() {
  let vista = '';
  try { vista = localStorage.getItem('dallanaNovedades') || ''; } catch {}
  if (vista !== NOVEDADES.version) setTimeout(() => abrirAlejandro(0), 1500);
}

$('alejandroSprite')?.addEventListener('click', () => {
  if (alejandroIgnorarClick) { alejandroIgnorarClick = false; return; }
  const globo = $('alejandroGlobo');
  if (globo && !globo.hidden) { cerrarAlejandro(false); return; }
  // si estaba durmiendo, primero despierta bostezando
  if ($('alejandro')?.dataset.estado === 'dormir') alejandroReacciona('bostezar', 1800);
  abrirAlejandro(0);
});
$('alejandroCerrar')?.addEventListener('click', () => cerrarAlejandro(false));
/* En el teléfono, Alejandro se agacha mientras haces scroll para no tapar nada */
let alejandroTimer = 0;
addEventListener('scroll', () => {
  const a = $('alejandro'), globo = $('alejandroGlobo');
  if (!a || innerWidth >= 600 || (globo && !globo.hidden)) return;
  a.classList.add('escondido');
  clearTimeout(alejandroTimer);
  alejandroTimer = setTimeout(() => a.classList.remove('escondido'), 1400);
}, { passive: true });
$('alejandroSiguiente')?.addEventListener('click', () => {
  if (alejandroPaso >= NOVEDADES.mensajes.length - 1) { cerrarAlejandro(true); return; }
  alejandroPaso++;
  pintarAlejandro();
});

/* ---------- Alejandro con vida: reacciona, duerme de noche, pasea y guarda un secreto ----------
   Estados (filas de assets/pixel/alejandro.png): salto, aplaudir, bailar, dormir, bostezar, caminar.
   Prioridad: una reacción del momento > música sonando > conversando > paseo > la hora del día. */
const MENSAJE_SECRETO = 'Papá te extraña muchísimo 💗';
const sinMovimiento = () => matchMedia('(prefers-reduced-motion: reduce)').matches;
let alejandroReaccion = null, alejandroReaccionTimer = 0, alejandroCaminando = false, alejandroCaminaTimer = 0;
let alejandroIgnorarClick = false, alejandroPresionTimer = 0;

function estadoPorHora() {
  const h = new Date().getHours();
  return (h >= 23 || h < 7) ? 'dormir' : 'salto';
}

function estadoAlejandro() {
  const a = $('alejandro'); if (!a) return;
  const globo = $('alejandroGlobo');
  let e;
  if (alejandroReaccion) e = alejandroReaccion;
  else if (musicAudio && !musicAudio.paused) e = 'bailar';
  else if (globo && !globo.hidden) e = 'salto';
  else if (alejandroCaminando) e = 'caminar';
  else e = estadoPorHora();
  a.dataset.estado = e;
}

function alejandroReacciona(tipo, ms) {
  alejandroReaccion = tipo;
  alejandroCaminando = false;
  clearTimeout(alejandroReaccionTimer);
  alejandroReaccionTimer = setTimeout(() => { alejandroReaccion = null; estadoAlejandro(); }, ms);
  estadoAlejandro();
}

/* De vez en cuando sale a pasear de lado, como los cangrejos, y vuelve a su esquina */
function programarPaseo() {
  setTimeout(() => {
    const a = $('alejandro'), globo = $('alejandroGlobo');
    const libre = a && globo && globo.hidden && !alejandroReaccion && !(musicAudio && !musicAudio.paused)
      && estadoPorHora() === 'salto' && !a.classList.contains('escondido') && document.visibilityState === 'visible';
    if (libre && !sinMovimiento()) {
      alejandroCaminando = true;
      estadoAlejandro();
      clearTimeout(alejandroCaminaTimer);
      alejandroCaminaTimer = setTimeout(() => { alejandroCaminando = false; estadoAlejandro(); }, 9000);
    }
    programarPaseo();
  }, 25000 + Math.random() * 30000);
}

/* Baila mientras suena la música */
if (musicAudio) ['play', 'pause', 'ended'].forEach(ev => musicAudio.addEventListener(ev, estadoAlejandro));

/* Revisa la hora: si se hace de día, se despierta bostezando */
let alejandroUltimaHora = estadoPorHora();
setInterval(() => {
  const ahora = estadoPorHora();
  if (alejandroUltimaHora === 'dormir' && ahora === 'salto') alejandroReacciona('bostezar', 3600);
  alejandroUltimaHora = ahora;
  estadoAlejandro();
}, 60000);

/* Mantenerlo presionado muestra el mensaje secreto */
function mostrarSecretoAlejandro() {
  const globo = $('alejandroGlobo'); if (!globo) return;
  const texto = $('alejandroTexto'), paso = $('alejandroPaso'), sig = $('alejandroSiguiente');
  if (texto) texto.textContent = MENSAJE_SECRETO;
  if (paso) paso.textContent = '🤫 secreto';
  if (sig) sig.hidden = true;
  alejandroSecreto = true;
  globo.hidden = false;
  $('alejandroSprite')?.setAttribute('aria-expanded', 'true');
  alejandroReacciona('aplaudir', 2400);
  lanzarCelebracion();
  try { navigator.vibrate?.(40); } catch {}
  notificar('descubrió el mensaje secreto de Alejandro 🤫', 'crab');
}
(() => {
  const spr = $('alejandroSprite'), a = $('alejandro');
  if (!spr || !a) return;
  const soltar = () => { clearTimeout(alejandroPresionTimer); a.classList.remove('presionando'); };
  spr.addEventListener('pointerdown', e => {
    if (e.button > 0) return;
    a.classList.add('presionando');
    clearTimeout(alejandroPresionTimer);
    alejandroPresionTimer = setTimeout(() => {
      a.classList.remove('presionando');
      alejandroIgnorarClick = true;
      setTimeout(() => { alejandroIgnorarClick = false; }, 1200);
      mostrarSecretoAlejandro();
    }, 700);
  });
  ['pointerup', 'pointerleave', 'pointercancel'].forEach(ev => spr.addEventListener(ev, soltar));
  spr.addEventListener('contextmenu', e => e.preventDefault());
})();

/* ============================================================
   INICIALIZACIÓN
   ============================================================ */
avisarVisita();
actualizarContador();
registrarDia();
actualizarProgreso();
if (!$('welcome')) saludoAlejandro();
estadoAlejandro();
{ const h = new Date().getHours(); if (h >= 7 && h < 11) setTimeout(() => alejandroReacciona('bostezar', 3600), 900); }
programarPaseo();
actualizarBotonFavoritos();
renderContenido();
cargarContenido();
setInterval(actualizarContador, 60000);

if ('serviceWorker' in navigator && (location.protocol === 'https:' || location.hostname === 'localhost' || location.hostname === '127.0.0.1')) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('./sw.js').catch(() => {});
  });
}

