/* ============================================================
   CONFIGURACIÓN
   ============================================================ */
const URL_BACKEND = '';
const FECHA_INICIO = '2026-10-17';
// Servidor del rincón en Cloudflare (ver rincon-servidor/GUIA.md). Vacío = funciona como antes, directo con ntfy.
// Con servidor: los temas de ntfy quedan ocultos, el buzón pide la clave de Dallana, las cartas no se pierden y su progreso se respalda.
const URL_RINCON = '';
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
    {titulo:'Tu vocación',descripcion:'Tu curiosidad por la geología y la dedicación que pones en tu carrera me inspiran.',mensaje:'Mi geóloga favorita.',icono:'geologa',tecnica:'Rocas, fósiles y mucha curiosidad',foto:''},
    {titulo:'Tu sonrisa',descripcion:'Tu sonrisa tiene el poder de arreglarme el día, aunque venga malo.',mensaje:'Mi lugar favorito del mundo.',icono:'sonrisa',tecnica:'Luz natural sobre un día cualquiera',foto:''},
    {titulo:'Tus gustos',descripcion:'Sushi, pizza, turrones y esos momentos simples que disfrutamos juntos.',mensaje:'Me gusta aprender qué cosas te hacen feliz.',icono:'gustos',tecnica:'Sushi, pizza y turrones sobre mesa compartida',foto:''},
    {titulo:'Nuestros paseos',descripcion:'Caminar contigo por Conce siempre es un buen plan.',mensaje:'A tu lado, cualquier camino se vuelve mi favorito.',icono:'paseos',tecnica:'Caminata larga por Conce',foto:''},
    {titulo:"Tu voz",descripcion:"Me encanta escucharte cantar; podría quedarme horas así.",mensaje:"Mi cantante favorita.",icono:'voz',tecnica:'Canto a capela',foto:''},
    {titulo:"Tu manera de cuidar",descripcion:"Siempre te preocupas de si llegué bien, de si comí, de cómo amanecí.",mensaje:"Me haces sentir muy querido.",icono:'cuidar',tecnica:'Mensajes de «¿llegaste bien?»',foto:''},
    {titulo:"Tu carácter",descripcion:"Defiendes lo que piensas con seguridad, y eso me encanta de ti.",mensaje:"Nunca dejes de hacerlo.",icono:'caracter',tecnica:'Convicción al óleo',foto:''},
    {titulo:"Tu lado divertido",descripcion:"Pasas de hablar súper en serio a decir una tontera en segundos.",mensaje:"Contigo me río de verdad.",icono:'divertida',tecnica:'Tonteras en tiempo récord',foto:''},
    {titulo:"Tu estilo",descripcion:"Me encanta tu forma de vestir; tiene algo muy tuyo.",mensaje:"Siempre te ves muy pero muy linda.",icono:'estilo',tecnica:'Moda propia, sin copiar a nadie',foto:''},
    {titulo:"Tus ojitos hermosos",descripcion:"Podría quedarme mirándolos por horas; dicen todo lo que sientes sin que hables.",mensaje:"Me pierdo en ellos cada vez.",icono:'ojitos',tecnica:'Mirada en técnica mixta',foto:''},
    {titulo:"La mejor cocinera del mundo",descripcion:"Todo lo que cocinas sabe a cariño, y eso no se aprende en ninguna receta.",mensaje:"Mi chef favorita, sin discusión.",icono:'cocinera',tecnica:'Receta secreta con cariño',foto:''}
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
const guardarJSON = (key, value) => { try { localStorage.setItem(key, JSON.stringify(value)); marcarRespaldo(); } catch {} };
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
/* Contador vivo (días, horas y minutos desde el inicio) y el próximo cumplemes */
function actualizarContador() {
  const [anio, mes, dia] = FECHA_INICIO.split('-').map(Number);
  const ahora = new Date();
  const inicio = new Date(anio, mes - 1, dia);
  const el = $('counter'); if (!el) return;
  const ms = ahora - inicio;
  if (ms < 0) { el.textContent = `Faltan ${Math.ceil(-ms / 864e5)} días para comenzar 💕`; return; }
  const dias = Math.floor(ms / 864e5) + 1, horas = ahora.getHours(), min = ahora.getMinutes();
  el.textContent = `${dias} ${dias === 1 ? 'día' : 'días'} · ${horas} h · ${String(min).padStart(2, '0')} min juntos`;
  // próximo cumplemes (cada día FECHA_INICIO.dia)
  const hito = $('coverHito'); if (!hito) return;
  const hoy = new Date(ahora.getFullYear(), ahora.getMonth(), ahora.getDate());
  let prox = new Date(hoy.getFullYear(), hoy.getMonth(), dia);
  if (prox < hoy) prox = new Date(hoy.getFullYear(), hoy.getMonth() + 1, dia);
  const meses = (prox.getFullYear() - anio) * 12 + prox.getMonth() - (mes - 1);
  const faltan = Math.round((prox - hoy) / 864e5);
  const nombreMeses = `${meses} ${meses === 1 ? 'mes' : 'meses'}`;
  hito.textContent = meses <= 0 ? '' : faltan === 0 ? `¡Hoy cumplimos ${nombreMeses}! 🎉` : `faltan ${faltan} ${faltan === 1 ? 'día' : 'días'} para los ${nombreMeses} 💗`;
}

/* La postal de Conce cambia con la hora: mañana, tarde o noche */
function pintarPostal() {
  const img = $('postalImg'); if (!img) return;
  const h = new Date().getHours();
  const momento = h >= 6 && h < 12 ? 'manana' : h >= 12 && h < 20 ? 'tarde' : 'noche';
  const src = `assets/pixel/postal-${momento}.png?v=1`;
  if (!img.getAttribute('src').endsWith(src)) img.src = src;
  // detrás asoma la postal de la hora que viene
  const atras = $('postalAtras');
  const siguiente = { manana: 'tarde', tarde: 'noche', noche: 'manana' }[momento];
  if (atras) atras.style.setProperty('--img', `url("assets/pixel/postal-${siguiente}.png?v=1")`);
}

/* Su nombre se escribe solo cuando se ve el encabezado por primera vez */
const coverEl = document.querySelector('.cover');
if (coverEl && !matchMedia('(prefers-reduced-motion: reduce)').matches) coverEl.classList.add('por-escribir');
function escribirNombre() {
  if (!coverEl || !coverEl.classList.contains('por-escribir') || coverEl.classList.contains('escribe')) return;
  coverEl.classList.add('escribe');
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
  { titulo: 'Estudiando juntos', imagen: 'assets/pixel/estudio.gif', frase: 'Dallana tratando de explicarme la materia y no estoy entendiendo nada' },
  { titulo: 'Los patitos de la pasarela', imagen: 'assets/pixel/pasarela.gif', frase: '' },
  { titulo: 'La pregunta en la pasarela', imagen: 'assets/pixel/pasarela2.gif', frase: '' }
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
    setTimeout(corazonGigante, 450);
    alejandroReacciona('enamorado', 3200);
    alejandroDice(`¡Llenaste los ${CORAZONES_POR_DIA} corazones de hoy, mamá! Papá va a estar feliz. 💗`, 'Alejandro 🦀', null, true);
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
      chispasCorazon(c);
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
  revelarRecuerdo();
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
  scene.classList.remove('rompe-sello');
  requestAnimationFrame(() => { scene.classList.add('is-opening'); romperSello(scene); });
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
  const vistas = obrasVistas();
  const delDia = obraDelDia(items.length);
  const total = String(items.length).padStart(2, '0');
  const el = (tag, cls, txt) => { const e = document.createElement(tag); if (cls) e.className = cls; if (txt != null) e.textContent = txt; return e; };
  items.forEach((item, i) => {
    const num = String(i + 1).padStart(2, '0');
    const icono = OBRAS_ICONOS.indexOf(item.icono);
    const obra = el('div', 'obra'); obra.dataset.tono = i % 4; obra.dataset.obra = item.titulo;
    if (i === delDia) obra.dataset.delDia = '';
    if (!vistas.has(item.titulo)) obra.dataset.nueva = '';
    const carta = el('button', 'obra-carta'); carta.type = 'button';
    carta.setAttribute('aria-pressed', 'false');
    carta.setAttribute('aria-label', `Obra ${num}: ${item.titulo}. Toca para darla vuelta.`);

    const frente = el('span', 'obra-cara obra-frente');
    const marco = el('span', 'obra-marco');
    const lienzo = el('span', 'obra-lienzo');
    const pixel = el('span', 'obra-pixel'); pixel.style.setProperty('--n', icono >= 0 ? icono : i % OBRAS_ICONOS.length);
    lienzo.append(pixel); marco.append(lienzo, el('span', 'obra-sello', '¡nueva!'));
    if (i === delDia) marco.append(el('span', 'obra-cinta', 'Obra del día ✦'));
    const placa = el('span', 'obra-placa');
    placa.append(el('span', 'obra-num', `N.º ${num} / ${total}`), el('strong', '', item.titulo));
    frente.append(marco, placa);

    const reverso = el('span', 'obra-cara obra-reverso');
    reverso.setAttribute('aria-hidden', 'true');
    const mini = el('span', 'obra-mini'); mini.style.setProperty('--n', pixel.style.getPropertyValue('--n'));
    const idIcono = OBRAS_ICONOS[pixel.style.getPropertyValue('--n')];
    const sticker = document.createElement('img');
    sticker.className = 'obra-sticker'; sticker.alt = ''; sticker.loading = 'lazy'; sticker.decoding = 'async';
    sticker.src = `assets/stickers/${item.sticker || STICKERS_OBRA[idIcono] || 'stikers2'}.png`;
    reverso.append(sticker);
    (ADORNOS_OBRA[idIcono] || [0, 1, 3]).forEach((n, k) => {
      const a = el('span', `obra-adorno obra-adorno--${k + 1}`); a.style.setProperty('--a', n); reverso.append(a);
    });
    reverso.append(el('span', 'obra-timbre', 'En tu colección'), mini,
      el('span', 'obra-num', `N.º ${num} · Edición única`), el('strong', 'obra-titulo', item.titulo),
      el('span', 'obra-desc', item.descripcion || item.mensaje));
    if (item.descripcion && item.mensaje) reverso.append(el('span', 'obra-firma', item.mensaje));
    reverso.append(el('span', 'obra-tecnica', `Técnica: ${item.tecnica || 'amor sobre lienzo'}`));

    carta.append(frente, reverso);
    carta.addEventListener('click', () => voltearObra(obra, carta, item.titulo));
    obra.append(carta);
    host.append(obra);
  });
  pintarColeccion(items.length);
}

/* ---------- Museo de ti: cuadros que se dan vuelta, colección y Alejandro guía ----------
   Cada obra tiene un ícono pixel (assets/pixel/obras.png, lo genera propuesta/obras.py) elegido por «icono».
   Las obras que ya dio vuelta quedan en localStorage (dallanaObrasVistas); cada día una es «la obra del día». */
const OBRAS_ICONOS = ['geologa', 'sonrisa', 'gustos', 'paseos', 'voz', 'cuidar', 'caracter', 'divertida', 'estilo', 'ojitos', 'cocinera'];
// Sticker pegado en el reverso de cada obra (assets/stickers/<nombre>.png); una obra puede elegir otro con «sticker»
const STICKERS_OBRA = { geologa: 'stikers3', sonrisa: 'stikers16', gustos: 'stikers8', paseos: 'stikers4', voz: 'stikers12', cuidar: 'stikers5',
  caracter: 'stikers17', divertida: 'stikers18', estilo: 'stikers22', ojitos: 'stikers20', cocinera: 'stikers2' };
// Adornitos pixel del reverso (assets/pixel/adornos.png, propuesta/adornos.py):
// 0 corazón, 1 estrella, 2 flor, 3 chispa, 4 nota, 5 nube, 6 gema, 7 hongo, 8 cangrejito, 9 sobre
const ADORNOS_OBRA = { geologa: [6, 1, 3], sonrisa: [3, 0, 5], gustos: [7, 0, 3], paseos: [2, 5, 0], voz: [4, 3, 0], cuidar: [9, 0, 2],
  caracter: [1, 3, 0], divertida: [8, 4, 1], estilo: [2, 3, 0], ojitos: [3, 0, 1], cocinera: [7, 0, 3] };
const OBRAS_VISTAS = 'dallanaObrasVistas';
const DISFRAZ_GUIA = { id: 'guia-de-museo', nombre: 'guía de museo', frase: '¡Bienvenida al Museo de ti, mamá! Soy tu guía. 🎟️ Toca un cuadro para darlo vuelta.' };
const FRASES_GUIA = [
  'Esta es de mis favoritas, mamá. Papá dice que es idéntica al original. 🖼️',
  'Shhh… en el museo se habla bajito. Pero esta obra me hace aplaudir. 👏',
  'Fíjate en los detalles, mamá: papá la pintó mirándote. 🎨',
  'Esta no tiene precio, mamá. Es edición única… como tú. ✨',
  'Dicen que el artista se inspiró en una geóloga preciosa. 🦀',
  'Mamá, esta obra la cuido yo personalmente. Nadie la toca. 🛡️'
];
let guiaBolsa = [];
const GUIA_MAX = 120000;

// Si a los 2 minutos sigue de guía (por ejemplo, porque estaba hablando o caminando), se cambia igual
function quitarGuia() {
  if (disfrazActual !== DISFRAZ_GUIA) return;
  const pijama = DISFRACES.find(d => d.id === 'pijama');
  if (estadoPorHora() === 'dormir') ponerDisfraz(pijama, false);
  else ponerDisfraz(disfrazDelDia() || siguienteDisfraz(), true);
  programarDisfraz(120000 + Math.random() * 120000);
}

function obrasVistas() {
  try { return new Set(JSON.parse(localStorage.getItem(OBRAS_VISTAS) || '[]')); } catch { return new Set(); }
}

function obraDelDia(n) {
  if (!n) return -1;
  const dias = Math.floor(new Date(`${hoyLocal()}T12:00:00`).getTime() / 864e5);
  return ((dias * 7) % n + n) % n;
}

function pintarColeccion(total) {
  const host = $('museoColeccion'); if (!host) return;
  const titulos = [...document.querySelectorAll('#museumGrid .obra')].map(o => o.dataset.obra);
  const vistas = obrasVistas();
  const n = titulos.filter(t => vistas.has(t)).length;
  $('museoCuenta').textContent = `${n} de ${total}`;
  const puntos = $('museoPuntos'); puntos.replaceChildren();
  titulos.forEach(t => { const p = document.createElement('i'); if (vistas.has(t)) p.className = 'on'; puntos.append(p); });
  host.classList.toggle('completa', total > 0 && n === total);
}

function voltearObra(obra, carta, titulo) {
  const volteada = obra.classList.toggle('volteada');
  carta.setAttribute('aria-pressed', String(volteada));
  carta.querySelector('.obra-frente').setAttribute('aria-hidden', String(volteada));
  carta.querySelector('.obra-reverso').setAttribute('aria-hidden', String(!volteada));
  if (!volteada) return;
  const vistas = obrasVistas();
  if (vistas.has(titulo)) return;
  // primera vez que la da vuelta: entra a la colección
  vistas.add(titulo);
  try { localStorage.setItem(OBRAS_VISTAS, JSON.stringify([...vistas])); } catch { /* sin almacenamiento */ }
  delete obra.dataset.nueva;
  obra.classList.add('timbrando');
  chispasCorazon(obra.querySelector('.obra-reverso'));
  const total = document.querySelectorAll('#museumGrid .obra').length;
  pintarColeccion(total);
  const completa = $('museoColeccion')?.classList.contains('completa');
  if (estadoPorHora() === 'dormir') return;
  if (completa) {
    alejandroReacciona('aplaudir', 2400);
    alejandroDice('¡Mamá, viste todas las obras del Museo de ti! Te ganaste el pase dorado. 🎟️✨', 'Alejandro guía de museo 🦀');
  } else if (disfrazActual === DISFRAZ_GUIA) {
    if (!guiaBolsa.length) guiaBolsa = [...FRASES_GUIA].sort(() => Math.random() - .5);
    alejandroReacciona('aplaudir', 1400);
    alejandroDice(guiaBolsa.pop(), `Obra: ${titulo}`);
  }
}

// Al llegar al museo, Alejandro se pone su gorrita de guía (una vez por visita)
(() => {
  const sec = $('museumSection');
  if (!sec || !('IntersectionObserver' in window)) return;
  const io = new IntersectionObserver(entradas => {
    if (!entradas.some(e => e.isIntersecting)) return;
    if (!disfracesIniciados || estadoPorHora() === 'dormir' || document.querySelector('dialog[open]')) return;
    io.disconnect();
    ponerDisfraz(DISFRAZ_GUIA, true);
    // de guía dura 2 minutos como máximo: después vuelve sí o sí a sus otros disfraces
    programarDisfraz(GUIA_MAX);
    setTimeout(quitarGuia, GUIA_MAX + 1000);
  }, { threshold: .35 });
  io.observe(sec);
})();

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
  const rectSobre = (env || openEnvelopeBtn).getBoundingClientRect();
  if (cover) cover.classList.add('opening');
  notificar('abrió el sobre de la portada', 'envelope_with_arrow');
  const lento = !matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (lento) {
    vibrar();
    chispasCorazon(document.querySelector('.sobre-sello'));
    setTimeout(() => chispasCorazon(document.querySelector('.sobre-carta')), 1300);
  }
  setTimeout(() => {
    // «opening» se queda hasta que termina de desvanecerse (si no, el sobre se vuelve a armar mientras se va)
    if (cover) { cover.classList.add('closed'); setTimeout(() => cover.classList.remove('opening'), 900); }
    pedir(`${URL_BACKEND}/api/momento`, 'Un mensaje para ti');
    setTimeout(escribirNombre, 500);
    entradaAlejandro(rectSobre).then(saludoAlejandro);
  }, lento ? 1950 : 0);
};

/* ---------- Portada: saludo según la hora, post-it con el día, globito de Alejandro y escritorio que responde ---------- */
(() => {
  const cover = $('welcome'); if (!cover) return;
  const movimiento = !matchMedia('(prefers-reduced-motion: reduce)').matches;
  const h = new Date().getHours();
  const saludo = h >= 6 && h < 12 ? 'Buenos días' : h >= 12 && h < 20 ? 'Buenas tardes' : 'Buenas noches';
  const elSaludo = $('portadaSaludo'); if (elSaludo) elSaludo.textContent = `${saludo}, mi Dallana ♥`;
  // el mantel cambia con la hora: mantequilla en la mañana, cereza en la tarde y azul tinta de noche
  cover.classList.toggle('noche', h >= 20 || h < 6);
  cover.classList.toggle('manana', h >= 6 && h < 12);

  // Post-it: día de nosotros (y cumplemes los 17)
  const [anio, mes, dia] = FECHA_INICIO.split('-').map(Number);
  const ahora = new Date();
  const dias = Math.round((Date.UTC(ahora.getFullYear(), ahora.getMonth(), ahora.getDate()) - Date.UTC(anio, mes - 1, dia)) / 864e5) + 1;
  const meses = (ahora.getFullYear() - anio) * 12 + ahora.getMonth() - (mes - 1);
  if (ahora.getDate() === dia && meses > 0) {
    $('portadaDia').textContent = '¡Cumplemes!';
    $('portadaDiaTexto').textContent = `${meses} ${meses === 1 ? 'mes' : 'meses'} juntos 🎉`;
  } else if (dias > 0) {
    $('portadaDia').textContent = `Día ${dias}`;
  }
  const fecha = ahora.toLocaleDateString('es-CL', { weekday: 'long', day: 'numeric', month: 'long' });
  $('portadaFecha').textContent = fecha.charAt(0).toUpperCase() + fecha.slice(1);

  // Alejandro escribe su globito letra por letra
  const globo = $('portadaGlobo');
  const texto = h >= 20 || h < 6 ? '¡Mamá! Llegó una carta de noche… ¿la abres? 🌙' : '¡Mamá! Te llegó una carta… ¿la abres? 💌';
  if (globo) {
    if (!movimiento) { globo.textContent = texto; globo.classList.add('visible'); }
    else setTimeout(() => {
      if (cover.classList.contains('closed')) return;
      globo.classList.add('visible');
      const letras = [...texto]; let i = 0;
      const t = setInterval(() => { globo.textContent = letras.slice(0, ++i).join(''); if (i >= letras.length) clearInterval(t); }, 38);
    }, 1500);
  }

  // Guirnalda de lucecitas colgando en festones de lado a lado
  const luces = $('portadaLuces');
  const COLORES_LUZ = ['#ffd36b', '#ff8fa3', '#ff5a5f', '#8fb8ff', '#9be28c'];
  function colgarLuces() {
    if (!luces || cover.classList.contains('closed')) return;
    const W = innerWidth, chico = W < 600;
    if (!W) return;
    const tramo = W / (chico ? 2 : W < 1100 ? 3 : 4), hondo = chico ? 34 : 54, sep = chico ? 32 : 44;
    const y = x => 6 + hondo * Math.sin(Math.PI * ((x % tramo) / tramo));
    let d = '';
    for (let x = 0; x <= W; x += 6) d += `${x ? 'L' : 'M'}${x} ${y(x).toFixed(1)}`;
    luces.innerHTML = `<svg viewBox="0 0 ${W} 110" preserveAspectRatio="none"><path d="${d}" fill="none" stroke="#5a3a22" stroke-width="1.6"/></svg>`;
    for (let x = sep / 2, k = 0; x < W; x += sep, k++) {
      const b = document.createElement('i');
      b.style.left = `${x}px`; b.style.top = `${y(x) + 3}px`;
      b.style.setProperty('--c', COLORES_LUZ[k % COLORES_LUZ.length]);
      b.style.setProperty('--d', `${-(Math.random() * 2.6).toFixed(2)}s`);
      luces.append(b);
    }
  }
  colgarLuces();
  let lucesTimer = 0;
  addEventListener('resize', () => { clearTimeout(lucesTimer); lucesTimer = setTimeout(colgarLuces, 200); });

  // Las cosas del escritorio saltan al tocarlas
  cover.querySelectorAll('.portada-cosa').forEach(c => c.addEventListener('click', () => {
    c.classList.remove('mueve'); void c.offsetWidth; c.classList.add('mueve');
  }));

  // En PC el sobre se inclina siguiendo el mouse
  const env = $('env');
  if (env && movimiento && matchMedia('(pointer: fine)').matches) {
    cover.addEventListener('pointermove', e => {
      if (cover.classList.contains('opening')) return;
      const dx = e.clientX / innerWidth - .5, dy = e.clientY / innerHeight - .5;
      env.style.setProperty('--ry', `${(dx * 14).toFixed(2)}deg`);
      env.style.setProperty('--rx', `${(-dy * 10).toFixed(2)}deg`);
    });
  }
})();

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
  const sec = openLetterBtn.closest('.letter-feature');
  if (sec?.classList.contains('abriendo')) return;
  cargarCarta();
  notificar('abrió tu carta principal 💌', 'love_letter');
  const abrir = () => {
    lanzarCelebracion();
    const dlg = $('letterDialog'); if (dlg && !dlg.open) dlg.showModal();
    // al cerrarla, la carta vuelve a quedar atada y sellada
    setTimeout(() => sec?.classList.remove('abriendo'), 900);
  };
  if (!sec || matchMedia('(prefers-reduced-motion: reduce)').matches) { abrir(); return; }
  // se suelta el cordel, salta el sello y después se abre la carta
  sec.classList.add('abriendo');
  vibrar();
  setTimeout(abrir, 650);
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
    if (URL_RINCON) {
      if (tokenRincon) rincon('/api/aviso', { method: 'POST', keepalive: true, body: JSON.stringify({ titulo, texto: `${quienVisita} ${texto}`, tags }) }).catch(() => {});
      return;
    }
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
  version: '2026-11-20b',
  mensajes: [
    '¡Hola, Dallana! Me llamo Alejandro y te voy a mostrar las novedades de este espacio. 🦀',
    '¡Ahora también soy cartero! 📬 A mi lado está nuestro buzón: ahí llegan las cartas de papá y yo te las traigo.',
    'Y si quieres decirle algo a papá, toca el buzón y elige «Escríbele a papá». Yo se lo llevo al tiro. 💌',
    'Ah… y tengo un secreto. Mantenme presionado un ratito para descubrirlo. 🤫',
    '¡Eso es todo por ahora! Tócame cuando quieras.'
  ]
};
let alejandroPaso = 0;

let alejandroModo = 'novedades';   // novedades | menu | secreto

function modoGlobo(modo) {
  alejandroModo = modo;
  const menu = $('alejandroMenu'), pie = document.querySelector('.alejandro-pie');
  if (menu) menu.hidden = modo !== 'menu';
  if (pie) pie.hidden = modo === 'menu';
}

function pintarAlejandro() {
  const texto = $('alejandroTexto'), paso = $('alejandroPaso'), sig = $('alejandroSiguiente');
  const total = NOVEDADES.mensajes.length;
  modoGlobo('novedades');
  if (sig) sig.hidden = false;
  if (texto) texto.textContent = NOVEDADES.mensajes[alejandroPaso];
  if (paso) paso.textContent = `${alejandroPaso + 1} de ${total}`;
  if (sig) sig.textContent = alejandroPaso === total - 1 ? '¡Listo!' : 'Siguiente ›';
}

function abrirAlejandro(desde = 0) {
  const globo = $('alejandroGlobo'); if (!globo) return;
  if (document.querySelector('dialog[open]')) { setTimeout(() => abrirAlejandro(desde), 3000); return; }
  if (!enCasa()) { volverACasa(() => abrirAlejandro(desde), true); return; }
  alejandroPaso = desde;
  pintarAlejandro();
  globo.hidden = false;
  $('alejandroSprite')?.setAttribute('aria-expanded', 'true');
  estadoAlejandro();
}

function cerrarAlejandro(leido) {
  const globo = $('alejandroGlobo'); if (!globo) return;
  const estabaAbierto = !globo.hidden;
  globo.hidden = true;
  $('alejandroSprite')?.setAttribute('aria-expanded', 'false');
  estadoAlejandro();
  if (estabaAbierto) setTimeout(decirPendientes, 700);
  if (alejandroModo === 'tutorial') {
    $('buzonEsquina')?.classList.remove('resaltado');
    try { localStorage.setItem('dallanaTutorialBuzon', '1'); } catch {}
    alejandroModo = 'novedades';
    if (cartaPendiente()) setTimeout(avisarCartaNueva, 800);
    return;
  }
  if (alejandroModo !== 'novedades') return;
  try { localStorage.setItem('dallanaNovedades', NOVEDADES.version); } catch {}
  if (leido) notificar('leyó las novedades de Alejandro 🦀', 'crab');
  if (tutorialPendiente()) setTimeout(abrirTutorialBuzon, 700);
}

function saludoAlejandro() {
  subirAlejandro();
  empezarDisfraces();
  empezarCartero();
  setTimeout(saludoDeRegreso, 2600);
  setTimeout(revisarRutinas, 9000);
  let vista = '';
  try { vista = localStorage.getItem('dallanaNovedades') || ''; } catch {}
  if (vista !== NOVEDADES.version) setTimeout(() => abrirAlejandro(0), 1500);
  else if (tutorialPendiente()) setTimeout(abrirTutorialBuzon, 2500);
}

$('alejandroSprite')?.addEventListener('click', () => {
  if (alejandroIgnorarClick) { alejandroIgnorarClick = false; return; }
  const globo = $('alejandroGlobo');
  if (globo && !globo.hidden) { cerrarAlejandro(false); return; }
  cancelarPaseo();
  // si estaba durmiendo, primero despierta bostezando
  if ($('alejandro')?.dataset.estado === 'dormir') alejandroReacciona('bostezar', 1800);
  const carta = cartaPendiente();
  if (carta) { volverACasa(() => abrirCartaPapa(carta), true); return; }
  abrirMenuAlejandro();
});
$('alejandroCerrar')?.addEventListener('click', () => cerrarAlejandro(false));
/* En el teléfono, Alejandro se agacha mientras haces scroll para no tapar nada */
let alejandroTimer = 0;
addEventListener('scroll', () => {
  const a = $('alejandro'), globo = $('alejandroGlobo');
  if (!a || innerWidth >= 600 || (globo && !globo.hidden) || !enCasa()) return;
  const bz = $('buzonEsquina');
  a.classList.add('escondido'); bz?.classList.add('escondido');
  clearTimeout(alejandroTimer);
  alejandroTimer = setTimeout(() => { a.classList.remove('escondido'); bz?.classList.remove('escondido'); }, 1400);
}, { passive: true });
$('alejandroSiguiente')?.addEventListener('click', () => {
  if (alejandroModo === 'tutorial') {
    if (tutorialPaso >= TUTORIAL_BUZON.length - 1) { cerrarAlejandro(true); return; }
    tutorialPaso++;
    pintarTutorial();
    return;
  }
  if (alejandroPaso >= NOVEDADES.mensajes.length - 1) { cerrarAlejandro(true); return; }
  alejandroPaso++;
  pintarAlejandro();
});

/* ---------- Alejandro con vida: reacciona, duerme de noche, pasea y guarda un secreto ----------
   Estados (filas de assets/pixel/alejandro.png, las genera propuesta/alejandro2.py):
     0 salto · 1 aplaudir · 2 bailar · 3 dormir · 4 bostezar · 5 caminar
     6 saludar · 7 llorar (de emoción) · 8 enamorado · 9 enojado (de mentirita) · 10 mareado
   Prioridad: una reacción del momento > música sonando > conversando > paseo > la hora del día.
   Sus horas están en HORAS_ALEJANDRO (dormir y rutinas); la portada usa su propia noche visual (20–6). */
const MENSAJE_SECRETO = 'Papá te extraña muchísimo 💗';
const sinMovimiento = () => matchMedia('(prefers-reduced-motion: reduce)').matches;
let alejandroReaccion = null, alejandroReaccionTimer = 0, alejandroCaminando = false;
let alejandroIgnorarClick = false, alejandroPresionTimer = 0;

/* De noche (23:00–7:00) duerme, pero si Dallana hace algo en la página se despierta y hace lo mismo que de día.
   Si pasa INACTIVIDAD_DORMIR sin que ella haga nada, se vuelve a dormir con su pijama. */
const INACTIVIDAD_DORMIR = 90000;
const HORAS_ALEJANDRO = { dormirDesde: 23, despertar: 7 };
let despiertoDeNoche = false, inactividadTimer = 0, ultimaActividad = 0;

function esDeNoche() {
  const h = new Date().getHours();
  return h >= HORAS_ALEJANDRO.dormirDesde || h < HORAS_ALEJANDRO.despertar;
}

function estadoPorHora() {
  return (esDeNoche() && !despiertoDeNoche) ? 'dormir' : 'salto';
}

function actividadUsuario() {
  ultimaActividad = Date.now();
  if (!esDeNoche()) return;
  clearTimeout(inactividadTimer);
  inactividadTimer = setTimeout(dormirDeNuevo, INACTIVIDAD_DORMIR);
  if (!despiertoDeNoche) despertarDeNoche();
}

function despertarDeNoche() {
  despiertoDeNoche = true;
  alejandroReacciona('bostezar', 1800);
  if (disfracesIniciados) {
    setTimeout(() => alejandroDice('¡Mamá! ¿Tampoco puedes dormir? Te acompaño un ratito. 🦀', 'Alejandro 🦀'), 1900);
    programarDisfraz(20000);
  }
}

function dormirDeNuevo() {
  if (!esDeNoche() || !despiertoDeNoche) return;
  despiertoDeNoche = false;
  const pijama = DISFRACES.find(d => d.id === 'pijama');
  volverACasa(() => { if (disfracesIniciados) ponerDisfraz(pijama, false); estadoAlejandro(); });
  estadoAlejandro();
  programarDisfraz(180000);
}

['pointerdown', 'keydown', 'scroll', 'wheel', 'touchstart'].forEach(ev => addEventListener(ev, actividadUsuario, { passive: true }));

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

/* ---------- Paseo libre: camina de lado por toda la pantalla y vuelve a su esquina ----------
   Nunca pasa por encima del texto de una carta abierta. Se mueve con la propiedad CSS «translate»
   (así no choca con el «transform» que lo agacha al hacer scroll en el teléfono). */
const VEL_PASEO = 70;                // píxeles por segundo
let alejandroPos = { x: 0, y: 0 }, paseoId = 0, paseoTimer = 0, alejandroMoviendo = false;
// En casa = llegó a su esquina (no solo que va hacia ella: mientras camina tiene «translate» y los globos fijos del teléfono se angostan)
const enCasa = () => !alejandroMoviendo && Math.abs(alejandroPos.x) < 1 && Math.abs(alejandroPos.y) < 1;

function zonasCarta() {
  const sel = '#letterDialog[open] .letter-paper, #letterDialog[open] .letter-head, #openWhenDialog[open] .animated-note, '
    + '#openWhenDialog[open] h2, #cartaPapaDialog[open] .carta-papa-papel, #cartaPapaDialog[open] .buzon-lista, #paraPapaDialog[open] form';
  return [...document.querySelectorAll(sel)].map(e => e.getBoundingClientRect()).filter(r => r.width > 0 && r.height > 0);
}

/* Caja del cangrejo (sin el margen transparente de la hoja) cuando está en su esquina */
function cajaEnCasa() {
  const spr = $('alejandroSprite'); if (!spr) return null;
  const r = spr.getBoundingClientRect();
  const left = r.left + r.width * .16 - alejandroActual().x, top = r.top + r.height * .16 - alejandroActual().y;
  return { left, top, right: left + r.width * .68, bottom: top + r.height * .84 };
}

function alejandroActual() {
  const a = $('alejandro'); if (!a) return { x: 0, y: 0 };
  const t = getComputedStyle(a).translate;
  if (!t || t === 'none') return { x: 0, y: 0 };
  const [x, y] = t.split(' ').map(v => parseFloat(v) || 0);
  return { x, y: y || 0 };
}

function chocaConCartas(caja, zonas, x, y) {
  const m = 10;
  return zonas.some(z => caja.left + x < z.right + m && caja.right + x > z.left - m && caja.top + y < z.bottom + m && caja.bottom + y > z.top - m);
}

function caminoLibre(caja, zonas, desde, hasta) {
  const dist = Math.hypot(hasta.x - desde.x, hasta.y - desde.y);
  const pasos = Math.max(1, Math.ceil(dist / 12));
  for (let k = 1; k <= pasos; k++) {
    const t = k / pasos;
    if (chocaConCartas(caja, zonas, desde.x + (hasta.x - desde.x) * t, desde.y + (hasta.y - desde.y) * t)) return false;
  }
  return true;
}

function limitesPaseo(caja) {
  const m = 8;
  return { minX: m - caja.left, maxX: innerWidth - m - caja.right, minY: m - caja.top, maxY: innerHeight - m - caja.bottom };
}

function elegirDestino(exigirCamino = true) {
  const caja = cajaEnCasa(); if (!caja) return null;
  const zonas = zonasCarta(), lim = limitesPaseo(caja), desde = alejandroActual();
  if (lim.maxX < lim.minX || lim.maxY < lim.minY) return null;
  for (let k = 0; k < 30; k++) {
    const p = { x: lim.minX + Math.random() * (lim.maxX - lim.minX), y: lim.minY + Math.random() * (lim.maxY - lim.minY) };
    if (Math.hypot(p.x - desde.x, p.y - desde.y) < 80) continue;
    if (chocaConCartas(caja, zonas, p.x, p.y)) continue;
    if (exigirCamino && !caminoLibre(caja, zonas, desde, p)) continue;
    return p;
  }
  return null;
}

/* Lo mueve hasta (x, y). Devuelve una promesa que se cumple al llegar (o false si lo interrumpen). */
function caminarA(p, rapido = false, vel = VEL_PASEO) {
  const a = $('alejandro'); if (!a) return Promise.resolve(false);
  const id = paseoId;
  const desde = alejandroActual();
  const dist = Math.hypot(p.x - desde.x, p.y - desde.y);
  const seg = rapido ? Math.min(.6, dist / 600) : dist / vel;
  alejandroCaminando = !rapido && dist > 2;
  // al caminar se le pasa la reacción del momento (si no, caminaría con la pose de aplaudir o enamorado)
  if (alejandroCaminando && alejandroReaccion) { clearTimeout(alejandroReaccionTimer); alejandroReaccion = null; }
  estadoAlejandro();
  a.style.transition = `translate ${seg}s linear, transform .35s ease, opacity .35s ease`;
  a.style.translate = `${p.x}px ${p.y}px`;
  alejandroPos = { x: p.x, y: p.y };
  alejandroMoviendo = dist > 1;
  if (alejandroMoviendo) { const dice = $('alejandroDice'); if (dice) dice.hidden = true; }
  return new Promise(res => setTimeout(() => {
    if (id !== paseoId) return res(false);
    alejandroMoviendo = false;
    // en su esquina queda sin «translate»: si no, los globos fijos del teléfono toman su ancho
    if (Math.abs(p.x) < 1 && Math.abs(p.y) < 1) { a.style.transition = 'transform .35s ease, opacity .35s ease'; a.style.translate = ''; }
    alejandroCaminando = false;
    estadoAlejandro();
    res(true);
  }, seg * 1000 + 30));
}

/* Lo deja quieto donde está (si lo interrumpen a medio camino) */
function detenerAqui() {
  const a = $('alejandro'); if (!a) return;
  const p = alejandroActual();
  a.style.transition = 'transform .35s ease, opacity .35s ease';
  // en su esquina, sin «translate» (aunque sea 0px: igual angostaría los globos fijos del teléfono)
  const quieto = Math.abs(p.x) < 1 && Math.abs(p.y) < 1;
  a.style.translate = quieto ? '' : `${p.x}px ${p.y}px`;
  alejandroPos = quieto ? { x: 0, y: 0 } : p;
  alejandroMoviendo = false;
  alejandroCaminando = false;
  estadoAlejandro();
}

function cancelarPaseo() {
  paseoId++;
  if (alejandroCaminando || alejandroMoviendo) detenerAqui();
}

function volverACasa(despues, rapido = false) {
  cancelarPaseo();
  const id = paseoId;
  if (enCasa()) { despues && despues(); return; }
  caminarA({ x: 0, y: 0 }, rapido).then(ok => { if (ok && id === paseoId && despues) despues(); });
}

const espera = ms => new Promise(r => setTimeout(r, ms));

async function pasear() {
  cancelarPaseo();
  const id = paseoId;
  const paradas = 1 + Math.floor(Math.random() * 3);
  for (let k = 0; k < paradas; k++) {
    const destino = elegirDestino();
    if (!destino) break;
    if (!(await caminarA(destino)) || id !== paseoId) return;
    await espera(2000 + Math.random() * 3500);
    if (id !== paseoId) return;
  }
  // de vuelta a su esquina, si el camino no cruza una carta
  const caja = cajaEnCasa();
  if (caja && !caminoLibre(caja, zonasCarta(), alejandroActual(), { x: 0, y: 0 })) return;
  await caminarA({ x: 0, y: 0 });
}

function programarPaseo() {
  clearTimeout(paseoTimer);
  paseoTimer = setTimeout(() => {
    const a = $('alejandro'), globo = $('alejandroGlobo'), dice = $('alejandroDice');
    const libre = a && globo && globo.hidden && (!dice || dice.hidden) && !alejandroReaccion && !(musicAudio && !musicAudio.paused)
      && estadoPorHora() === 'salto' && !a.classList.contains('escondido') && !a.classList.contains('oculto-carta')
      && document.visibilityState === 'visible';
    if (libre && !sinMovimiento()) pasear();
    programarPaseo();
  }, 20000 + Math.random() * 25000);
}

/* Cuando se abre una carta: Alejandro sube a la capa de arriba (para seguir viéndose) y se aparta del texto.
   Si no hay ningún lugar libre (cartas a pantalla completa en el teléfono), se esconde hasta que se cierre. */
function subirAlejandro() {
  const a = $('alejandro');
  if (!a || typeof a.showPopover !== 'function') return;
  try { if (a.matches(':popover-open')) a.hidePopover(); a.showPopover(); } catch {}
}

function apartarseDeCartas() {
  const a = $('alejandro'); if (!a) return;
  const caja = cajaEnCasa(); if (!caja) return;
  const zonas = zonasCarta();
  if (!zonas.length) { a.classList.remove('oculto-carta'); return; }
  cancelarPaseo();
  const aqui = alejandroActual();
  if (!chocaConCartas(caja, zonas, aqui.x, aqui.y)) { a.classList.remove('oculto-carta'); return; }
  // el lugar libre más cercano
  const lim = limitesPaseo(caja);
  let mejor = null, mejorD = Infinity;
  for (let k = 0; k < 160; k++) {
    const p = { x: lim.minX + Math.random() * (lim.maxX - lim.minX), y: lim.minY + Math.random() * (lim.maxY - lim.minY) };
    if (chocaConCartas(caja, zonas, p.x, p.y)) continue;
    const dd = Math.hypot(p.x - aqui.x, p.y - aqui.y);
    if (dd < mejorD) { mejor = p; mejorD = dd; }
  }
  if (mejor) { a.classList.remove('oculto-carta'); caminarA(mejor, true); }
  else a.classList.add('oculto-carta');
}

(() => {
  const dialogos = document.querySelectorAll('dialog');
  const obs = new MutationObserver(() => {
    const abierto = [...dialogos].some(d => d.open);
    if (abierto) {
      const dice = $('alejandroDice'); if (dice) dice.hidden = true;
      subirAlejandro(); setTimeout(apartarseDeCartas, 650);
    }
    else {
      const a = $('alejandro');
      if (a) a.classList.remove('oculto-carta');
      setTimeout(() => { if (!alejandroCaminando && !enCasa()) volverACasa(); }, 1200);
      setTimeout(decirPendientes, 1900);
    }
  });
  dialogos.forEach(d => obs.observe(d, { attributes: true, attributeFilter: ['open'] }));
  addEventListener('resize', () => { if ([...dialogos].some(d => d.open)) apartarseDeCartas(); });
})();

/* Baila mientras suena la música */
if (musicAudio) ['play', 'pause', 'ended'].forEach(ev => musicAudio.addEventListener(ev, estadoAlejandro));

/* Revisa la hora: si se hace de día, se despierta bostezando */
let alejandroEraNoche = esDeNoche();
setInterval(() => {
  const noche = esDeNoche();
  if (alejandroEraNoche && !noche) {
    // amaneció: si estaba durmiendo, despierta bostezando
    clearTimeout(inactividadTimer);
    const dormia = !despiertoDeNoche;
    despiertoDeNoche = false;
    if (dormia) alejandroReacciona('bostezar', 3600);
    programarDisfraz(5000);
  }
  if (!alejandroEraNoche && noche) {
    // anocheció: sigue despierto solo si ella está haciendo algo
    despiertoDeNoche = Date.now() - ultimaActividad < INACTIVIDAD_DORMIR;
    if (despiertoDeNoche) { clearTimeout(inactividadTimer); inactividadTimer = setTimeout(dormirDeNuevo, INACTIVIDAD_DORMIR - (Date.now() - ultimaActividad)); }
    else programarDisfraz(1000);
  }
  if (alejandroEraNoche !== noche) pintarCielo();
  alejandroEraNoche = noche;
  estadoAlejandro();
  revisarRutinas();
  marcarUltimaVez();
}, 60000);

/* ---------- Disfraces: cada cierto tiempo se cambia de disfraz al azar y dice una frase ----------
   Cada disfraz es una hoja de sprites en assets/pixel/disfraces/<id>.png (las genera propuesta/disfraces2.py --hojas).
   De noche, mientras duerme, usa el pijama. */
const DISFRACES = [
  ['aprendiz-de-mago', 'aprendiz de mago', '¡Mami, mira! ¡Wingardium Leviosa! ✨ Es leviÓsa, no leviosÁ.'],
  ['sombrero-que-habla', 'sombrero que habla', 'Mmm… difícil, muy difícil… ¡Ya sé! Te pongo en la casa del corazón de mamá. 🎩'],
  ['buscador-en-escoba', 'buscador en escoba', '¡Mami, atrapé la snitch dorada! ¡150 puntos para nosotros! 🧹'],
  ['brujita-de-pociones', 'brujita de pociones', 'Estoy preparando una poción de amor… pero creo que tú ya me la diste, mamá. 🧪'],
  ['hobbit-con-el-anillo', 'hobbit', 'Mi tesoro… 💍 ¡Mentira, mamá! Mi tesoro eres tú.'],
  ['el-mago-gris', 'mago gris', '¡No puedes pasaaar! …a menos que me des un abrazo, mamá. 🧙'],
  ['elfo-arquero', 'elfo arquero', 'Mamá, mis ojos de elfo ven algo hermoso a lo lejos… ¡eres tú! 🏹'],
  ['caballero-espacial', 'caballero espacial', 'Que la fuerza te acompañe, mamá. ✨'],
  ['el-lado-oscuro', 'lado oscuro', 'Mamá… yo soy tu cangrejo. 🖤'],
  ['maestro-verde', 'maestro verde', 'Adorable tú eres, mamá. Mucho amor en ti yo siento. 💚'],
  ['princesa-galactica', 'princesa galáctica', 'Ayúdame, mamá… eres mi única esperanza. 💫'],
  ['hombre-arana', 'hombre araña', 'Un gran poder conlleva una gran responsabilidad… y la mía es cuidarte, mamá. 🕸️'],
  ['capitan-del-escudo', 'capitán del escudo', 'Mamá, podría hacer esto todo el día. 🛡️'],
  ['dios-del-trueno', 'dios del trueno', '¡Mamá, soy digno! Levanté el martillo. ⚡'],
  ['armadura-de-hierro', 'armadura de hierro', 'Mamá, te quiero 3000. ❤️'],
  ['gigante-verde', 'gigante verde', '¿Mi secreto, mamá? Siempre estoy feliz… cuando estás tú. 💚'],
  ['hechicero-supremo', 'hechicero supremo', 'Vi 14.000.605 futuros, mamá… y en todos te quiero. 🔮'],
  ['murcielago', 'murciélago', 'Mamá, no le digas a nadie… ¡soy Batman! 🦇'],
  ['kriptoniano', 'kriptoniano', '¿Es un pájaro? ¿Es un avión? ¡No, mamá, soy yo! 💙'],
  ['amazona', 'amazona', '¡Mira, mamá, soy como tú! Fuerte, valiente y preciosa. ✨'],
  ['velocista', 'velocista', '¡Mamá, corrí tan rápido que llegué antes de que me extrañaras! ⚡'],
  ['rey-del-mar', 'rey del mar', 'Mamá, hablé con los peces y todos dicen que eres la más linda del mar. 🔱'],
  ['anillo-verde', 'anillo verde', 'En el día más brillante o la noche más oscura… siempre te voy a querer, mamá. 💚'],
  ['san-valentin', 'cupido', 'Mamá, ¿quieres ser mi San Valentín? 💘'],
  ['pijama', 'pijama', 'Mami, ¿me cuentas un cuento antes de dormir? 🧸'],
  ['navidad', 'Navidad', '¡Jo, jo, jo! Mamá, en mi carta a Santa solo pedí estar contigo. 🎄'],
  ['cumpleanos', 'cumpleaños', '¡Mamá, hagamos una fiesta! Cualquier día contigo hay que celebrarlo. 🎂'],
  ['fantasmita', 'fantasmita', '¡Buuu! ¿Te asusté, mamá? 👻 Es broma, soy yo, Alejandro.'],
  ['ano-nuevo', 'Año Nuevo', '¡Feliz año, mamá! Mi propósito es quererte todavía más. 🎆'],
  ['conejito-de-pascua', 'conejito', 'Mamá, te encontré un huevito de Pascua. 🐰'],
  ['chef', 'chef', 'Mamá, te cociné algo con mucho amor… ¿lo probamos? 🍳'],
  ['pirata', 'pirata', '¡Arrr! Encontré un tesoro, mamá… ¡y eres tú! 🏴‍☠️'],
  ['astronauta', 'astronauta', 'Mamá, fui hasta la Luna y volví solo para decirte que te quiero. 🚀'],
  ['graduado', 'graduado', '¡Me gradué, mamá! Con honores en quererte. 🎓'],
  ['vaquero', 'vaquero', '¡Yiii-ja! Mamá, en este pueblo no hay nadie más linda que tú. 🤠'],
  ['rey', 'rey', 'Mamá, tú eres la reina de este castillo. 👑'],
  ['hada', 'hada', 'Mamá, te concedo un deseo… ¿qué quieres? 🧚'],
  ['abejita', 'abejita', 'Bzzz… mamá, eres más dulce que la miel. 🐝'],
  ['marinero', 'marinero', '¡Ahoy, mamá! Navegué todos los mares y no encontré a nadie como tú. ⚓']
].map(([id, nombre, frase]) => ({ id, nombre, frase }));
let disfrazActual = null, disfrazBolsa = [], disfracesIniciados = false, alejandroDiceTimer = 0, disfrazTimer = 0;

function urlDisfraz(d) {
  return d ? `assets/pixel/disfraces/${d.id}.png?v=2` : 'assets/pixel/alejandro.png?v=5';
}

/* Lo que dice Alejandro en su globito chico. Devuelve true si lo dijo.
   Si hay una carta o su globo grande abiertos, no habla; lo «importante» (cartas de papá, recados,
   fechas especiales…) queda guardado y lo dice apenas se cierren (decirPendientes). */
let alejandroDiceAccion = null;
const dichosPendientes = [];
function alejandroDice(texto, titulo, accion = null, importante = false) {
  const el = $('alejandroDice'); if (!el) return false;
  const globo = $('alejandroGlobo');
  const ocupado = (globo && !globo.hidden) || document.querySelector('dialog[open]') || $('welcome')?.matches(':not(.closed)');
  if (ocupado) {
    if (importante && !dichosPendientes.some(d => d.texto === texto)) dichosPendientes.push({ texto, titulo, accion });
    if (dichosPendientes.length > 5) dichosPendientes.shift();
    return false;
  }
  if (!enCasa()) { volverACasa(() => alejandroDice(texto, titulo, accion, importante), true); return true; }
  const aside = $('alejandro'); if (aside && aside.style.translate) aside.style.translate = '';
  alejandroDiceAccion = accion;
  el.replaceChildren();
  const t = document.createElement('strong'); t.textContent = titulo;
  el.append(t, document.createTextNode(texto));
  el.hidden = false;
  clearTimeout(alejandroDiceTimer);
  alejandroDiceTimer = setTimeout(() => { el.hidden = true; decirPendientes(); }, Math.max(8000, texto.length * 70));
  return true;
}

function decirPendientes() {
  if (!dichosPendientes.length) return;
  const el = $('alejandroDice');
  if (el && !el.hidden) return;   // ya está diciendo algo: sigue cuando termine
  const d = dichosPendientes[0];
  if (alejandroDice(d.texto, d.titulo, d.accion)) dichosPendientes.shift();
}

/* «¡!» sobre su cabeza cuando algo lo sorprende */
function alejandroAlerta() {
  const spr = $('alejandroSprite'); if (!spr || sinMovimiento()) return;
  const a = document.createElement('span');
  a.className = 'alejandro-alerta'; a.textContent = '!'; a.setAttribute('aria-hidden', 'true');
  spr.append(a);
  setTimeout(() => a.remove(), 950);
}
$('alejandroDice')?.addEventListener('click', () => {
  $('alejandroDice').hidden = true;
  const accion = alejandroDiceAccion; alejandroDiceAccion = null;
  if (accion) accion();
});

function ponerDisfraz(d, hablar = true) {
  const spr = $('alejandroSprite'); if (!spr) return;
  if (d === disfrazActual) return;
  const img = new Image();
  img.onload = () => {
    disfrazActual = d;
    spr.style.backgroundImage = `url("${urlDisfraz(d)}")`;
    if (!sinMovimiento()) { spr.classList.remove('poof'); void spr.offsetWidth; spr.classList.add('poof'); setTimeout(() => spr.classList.remove('poof'), 750); }
    if (d && hablar) {
      alejandroDice(d.frase, `Alejandro ${d.nombre} 🦀`);
      if (estadoPorHora() !== 'dormir') alejandroReacciona('aplaudir', 1600);
    }
  };
  img.src = urlDisfraz(d);
}

function siguienteDisfraz() {
  if (!disfrazBolsa.length) {
    disfrazBolsa = DISFRACES.filter(d => d.id !== 'pijama' && d !== disfrazActual);
    for (let i = disfrazBolsa.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [disfrazBolsa[i], disfrazBolsa[j]] = [disfrazBolsa[j], disfrazBolsa[i]];
    }
  }
  return disfrazBolsa.pop();
}

function cambiarDisfraz() {
  const globo = $('alejandroGlobo');
  const pijama = DISFRACES.find(d => d.id === 'pijama');
  const especial = disfrazDelDia();
  if (estadoPorHora() === 'dormir') ponerDisfraz(pijama, false);
  else if (especial) { ponerDisfraz(especial, false); programarDisfraz(600000); return; }
  else if (document.visibilityState !== 'visible' || (globo && !globo.hidden) || alejandroCaminando || cartaPendiente()) { programarDisfraz(10000); return; }
  else ponerDisfraz(siguienteDisfraz(), true);
  programarDisfraz(120000 + Math.random() * 120000);   // el próximo, entre 2 y 4 minutos
}

function programarDisfraz(ms) {
  clearTimeout(disfrazTimer);
  disfrazTimer = setTimeout(cambiarDisfraz, ms);
}

function empezarDisfraces() {
  if (disfracesIniciados) return;
  disfracesIniciados = true;
  if (estadoPorHora() === 'dormir') ponerDisfraz(DISFRACES.find(d => d.id === 'pijama'), false);
  else if (disfrazDelDia()) ponerDisfraz(disfrazDelDia(), false);
  programarDisfraz(15000 + Math.random() * 25000);      // el primero, al ratito de entrar
}

/* ---------- Alejandro cartero: cartas de papá (por ntfy) y mensajes de Dallana para papá ----------
   Para mandarle una carta: escribe desde la app ntfy en el tema de avisos (donde te llegan las notificaciones)
   o en el tema NTFY_CARTAS. El título es opcional (no uses uno de TITULOS_DE_LA_PAGINA).
   Comandos: /borrar, /borrar 3, /borrar todo, /editar <texto>, /buzon (ver más abajo).
   ntfy.sh guarda los mensajes 12 horas: si Dallana no entra en ese tiempo, no le llega (te aviso cuando la recibe).
   Lo que ella le escribe a papá llega al tema de avisos (NTFY_TEMA), igual que la actividad. */
const NTFY_CARTAS = 'dallana-cartas-aaf3c4ba15';
let buzon = leerJSON('dallanaBuzon', []);
let carteroIniciado = false;
const guardarBuzon = () => {
  if (buzon.length > 80) buzon = buzon.slice(-80);
  guardarJSON('dallanaBuzon', buzon);
};
const cartaPendiente = () => buzon.find(c => c.de === 'papa' && !c.leida) || null;

function pintarSobre() {
  const sobre = $('alejandroSobre');
  if (sobre) sobre.hidden = !cartaPendiente();
  const n = buzon.filter(c => c.de === 'papa' && !c.leida).length;
  const badge = $('menuBuzonN'); if (badge) badge.textContent = n ? String(n) : '';
  pintarSeccionBuzon(n);
  const bz = $('buzonEsquina');
  if (bz) {
    bz.classList.toggle('con-carta', n > 0);
    bz.setAttribute('aria-label', n ? `Buzón de papá: ${n === 1 ? 'una carta nueva' : n + ' cartas nuevas'}` : 'Buzón de papá');
  }
  const bn = $('buzonEsquinaN'); if (bn) { bn.hidden = !n; bn.textContent = String(n); }
}

/* La sección «Buzón de papá» de la página: buzón con bandera, estado, última carta y botones */
function pintarSeccionBuzon(nuevas) {
  const sec = $('buzonSection'); if (!sec) return;
  const dePapa = buzon.filter(c => c.de === 'papa');
  const ultima = dePapa[dePapa.length - 1];
  sec.classList.toggle('tiene-cartas', nuevas > 0);
  const estado = $('buzonEstado');
  if (estado) estado.textContent = nuevas
    ? (nuevas === 1 ? '¡Tienes una carta nueva de papá! 💌' : `¡Tienes ${nuevas} cartas nuevas de papá! 💌`)
    : dePapa.length
      ? 'No hay cartas nuevas por ahora. Puedes releer las que te ha mandado o escribirle tú. 🦀'
      : 'Aquí llegan las cartas que papá te escribe. Alejandro te avisa apenas llega una. 🦀';
  const abrir = $('buzonAbrir'); if (abrir) abrir.hidden = !nuevas;
  const todas = $('buzonTodas'); if (todas) todas.textContent = buzon.length ? `📬 Ver todas las cartas (${buzon.length})` : '📬 Ver todas las cartas';
  const caja = $('buzonUltima');
  if (caja) {
    caja.hidden = !ultima || nuevas > 0;
    if (ultima) {
      $('buzonUltimaFecha').textContent = `Última carta · ${fechaCarta(ultima.t)}`;
      $('buzonUltimaTexto').textContent = ultima.texto;
      caja.onclick = () => abrirCartaPapa(ultima);
    }
  }
}

/* Tutorial: la primera vez Alejandro explica cómo funciona el buzón */
const TUTORIAL_BUZON = [
  'Mamá, este es nuestro buzón 📬. Aquí llegan las cartas que papá te escribe.',
  'Cuando la banderita está arriba, ¡hay una carta nueva! Toca el buzón para leerla. Yo también te aviso. 🦀',
  'Y si quieres decirle algo a papá, toca el buzón y elige «Escríbele a papá». Yo se lo llevo al tiro. 💌'
];
let tutorialPaso = 0;
const tutorialPendiente = () => { try { return localStorage.getItem('dallanaTutorialBuzon') !== '1'; } catch { return false; } };

function pintarTutorial() {
  const texto = $('alejandroTexto'), paso = $('alejandroPaso'), sig = $('alejandroSiguiente');
  if (texto) texto.textContent = TUTORIAL_BUZON[tutorialPaso];
  if (paso) paso.textContent = `${tutorialPaso + 1} de ${TUTORIAL_BUZON.length}`;
  if (sig) { sig.hidden = false; sig.textContent = tutorialPaso === TUTORIAL_BUZON.length - 1 ? '¡Entendido!' : 'Siguiente ›'; }
}

function abrirTutorialBuzon() {
  const globo = $('alejandroGlobo'); if (!globo || !globo.hidden) return;
  // con una carta o el juego abiertos, espera a que se cierren
  if (document.querySelector('dialog[open]')) { setTimeout(abrirTutorialBuzon, 3000); return; }
  if (!enCasa()) { volverACasa(abrirTutorialBuzon, true); return; }
  tutorialPaso = 0;
  modoGlobo('tutorial');
  pintarTutorial();
  globo.hidden = false;
  $('alejandroSprite')?.setAttribute('aria-expanded', 'true');
  $('buzonEsquina')?.classList.add('resaltado');
  estadoAlejandro();
}

$('buzonEsquina')?.addEventListener('click', () => {
  const c = cartaPendiente();
  if (c) abrirCartaPapa(c); else abrirBuzon();
});
$('menuAyudaBuzon')?.addEventListener('click', () => { cerrarAlejandro(false); setTimeout(abrirTutorialBuzon, 50); });
$('buzonAbrir')?.addEventListener('click', () => { const c = cartaPendiente(); if (c) abrirCartaPapa(c); });
$('buzonTodas')?.addEventListener('click', abrirBuzon);
$('buzonEscribir')?.addEventListener('click', abrirParaPapa);

function fechaCarta(t) {
  try { return new Date(t).toLocaleString('es-CL', { weekday: 'long', day: 'numeric', month: 'long', hour: '2-digit', minute: '2-digit' }); }
  catch { return ''; }
}

/* Papá puede escribir en cualquiera de los dos temas de ntfy:
   - NTFY_CARTAS: el tema propio de las cartas (todo lo que llega ahí es de papá).
   - NTFY_TEMA: el tema de avisos, donde papá recibe las notificaciones y suele responder desde la app.
     Ahí también publica la página, siempre con alguno de estos títulos; todo lo demás lo escribió papá.
   Comandos que papá puede escribir desde la app (nunca se le muestran a Dallana):
     /borrar          borra la última carta          /borrar 3     borra las últimas 3
     /borrar todo     borra las cartas de las últimas 12 horas
     /editar <texto>  reemplaza la última carta por <texto>
     /buzon           la página de Dallana responde qué cartas tiene y cuáles leyó
     /alejandro <frase>  Alejandro le dice <frase> de tu parte (con ojitos de corazón)
     /disfraz <nombre>   Alejandro se pone ese disfraz por 10 minutos (ej. /disfraz chef)
   Todo mensaje que empiece con «/» se trata como comando. */
const TITULOS_DE_LA_PAGINA = ['Actividad en tu pagina', 'Visita en tu pagina', 'Salio de tu pagina', 'Carta leida', 'Mensaje de Dallana 💌', 'Buzon de Dallana'];
// Las pruebas que papá mandó antes de este momento (20-11-2026 13:34) se ignoran
const CORTE_PRUEBAS = 1795192450;
const ultimoIdTema = {};
let cartasBorradas = new Set(leerJSON('dallanaCartasBorradas', []));
let comandosHechos = new Set(leerJSON('dallanaComandosHechos', []));
const guardarSetCorto = (clave, set) => guardarJSON(clave, [...set].slice(-300));

async function leerTema(tema, esDePapa) {
  const desde = ultimoIdTema[tema] || 'all';
  const r = await fetch(`https://ntfy.sh/${tema}/json?poll=1&since=${desde}`, { cache: 'no-store' });
  if (!r.ok) return [];
  const lista = [];
  for (const linea of (await r.text()).split('\n')) {
    if (!linea.trim()) continue;
    let m; try { m = JSON.parse(linea); } catch { continue; }
    if (m.event !== 'message') continue;
    ultimoIdTema[tema] = m.id;
    const texto = (m.message || '').trim();
    if (!texto || texto === 'triggered' || (m.time || 0) < CORTE_PRUEBAS || !esDePapa(m)) continue;
    lista.push({ id: m.id, t: (m.time || Date.now() / 1000) * 1000, titulo: m.title || '', texto });
  }
  return lista;
}

const sinTildes = t => (t || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').trim();
const DISFRAZ_CARTERO = { id: 'cartero', nombre: 'cartero', frase: '¡Cartero listo para el reparto, mamá! 📬' };
const cartasDePapaAntesDe = t => buzon.filter(c => c.de === 'papa' && c.t <= t).sort((a, b) => a.t - b.t);

function ejecutarComando(m) {
  if (comandosHechos.has(m.id)) return null;
  comandosHechos.add(m.id);
  const [orden, ...resto] = m.texto.slice(1).trim().split(/\s+/);
  const arg = resto.join(' ').trim();
  const cmd = (orden || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
  if (cmd === 'borrar') {
    let quitar;
    if (arg.toLowerCase() === 'todo') quitar = cartasDePapaAntesDe(m.t).filter(c => c.t >= m.t - 12 * 3600 * 1000);
    else quitar = cartasDePapaAntesDe(m.t).slice(-Math.max(1, Math.min(50, parseInt(arg, 10) || 1)));
    if (!quitar.length) return { aviso: 'no tenía cartas tuyas para borrar en el buzón 🧹' };
    quitar.forEach(c => cartasBorradas.add(c.id));
    buzon = buzon.filter(c => !cartasBorradas.has(c.id));
    const dlg = $('cartaPapaDialog');
    if (dlg?.open && quitar.some(c => $('cartaPapaTexto')?.textContent?.startsWith(c.texto.slice(0, 20)))) dlg.close();
    return { aviso: `ya no ve ${quitar.length === 1 ? '1 carta tuya' : quitar.length + ' cartas tuyas'}: Alejandro ${quitar.length === 1 ? 'la borró' : 'las borró'} del buzón 🧹` };
  }
  if (cmd === 'editar') {
    const ultima = cartasDePapaAntesDe(m.t).pop();
    if (!ultima || !arg) return { aviso: 'no tenía una carta tuya para corregir ✏️' };
    ultima.texto = arg;
    ultima.editada = true;
    ultima.leida = false;
    return { aviso: `tiene tu carta corregida en el buzón ✏️: «${arg.slice(0, 60)}${arg.length > 60 ? '…' : ''}»`, nueva: true };
  }
  if (cmd === 'alejandro') {
    if (!arg) return { aviso: 'no supe qué decirle: escribe /alejandro y tu frase 🦀' };
    alejandroReacciona('enamorado', 3000);
    alejandroDice(arg, 'Alejandro (recado de papá) 🦀', null, true);
    return { aviso: `ya tiene tu recado: Alejandro le dice «${arg.slice(0, 60)}${arg.length > 60 ? '…' : ''}» 🦀` };
  }
  if (cmd === 'disfraz') {
    const quiere = sinTildes(arg);
    const d = quiere && DISFRACES.concat([DISFRAZ_GUIA, DISFRAZ_CARTERO]).find(x => sinTildes(x.nombre) === quiere || x.id === quiere.replace(/\s+/g, '-'))
      || (quiere && DISFRACES.find(x => sinTildes(x.nombre).includes(quiere)));
    if (!d) return { aviso: `no encontré ese disfraz. Algunos: ${DISFRACES.slice(0, 12).map(x => x.nombre).join(', ')}… 🦀` };
    ponerDisfraz(d, true);
    programarDisfraz(600000);
    return { aviso: `Alejandro se puso el disfraz de ${d.nombre} 🦀` };
  }
  if (cmd === 'buzon') {
    const dePapa = buzon.filter(c => c.de === 'papa');
    const sinLeer = dePapa.filter(c => !c.leida).length;
    const detalle = dePapa.slice(-8).reverse().map(c => `${c.leida ? '✅' : '💌'} «${c.texto.slice(0, 40)}${c.texto.length > 40 ? '…' : ''}»`).join('\n');
    return { aviso: `tiene ${dePapa.length === 1 ? '1 carta tuya' : dePapa.length + ' cartas tuyas'} en el buzón (${sinLeer} sin leer)${detalle ? ':\n' + detalle : ''}`, titulo: 'Buzon de Dallana', tags: 'mailbox_with_mail' };
  }
  return null;
}

async function revisarCartas() {
  if (document.visibilityState !== 'visible') return;
  try {
    let mensajes;
    if (URL_RINCON) {
      if (!tokenRincon) return;
      const { cartas = [] } = await rincon('/api/cartas');
      mensajes = cartas.filter(m => m.t / 1000 >= CORTE_PRUEBAS);
    } else {
      const [a, b] = await Promise.all([
        leerTema(NTFY_CARTAS, () => true).catch(() => []),
        leerTema(NTFY_TEMA, m => !TITULOS_DE_LA_PAGINA.includes(m.title || '')).catch(() => [])
      ]);
      mensajes = [...a, ...b];
    }
    mensajes.sort((x, y) => x.t - y.t);
    const agregadas = [];
    let cambios = false, hayNueva = false;
    for (const m of mensajes) {
      if (m.texto.startsWith('/')) {
        const res = ejecutarComando(m);
        if (res) {
          cambios = true;
          if (res.nueva) hayNueva = true;
          notificar(res.aviso, res.tags || 'crab', res.titulo || 'Actividad en tu pagina');
        }
        continue;
      }
      if (cartasBorradas.has(m.id) || buzon.some(c => c.id === m.id)) continue;
      buzon.push({ id: m.id, de: 'papa', t: m.t, titulo: m.titulo, texto: m.texto, leida: false });
      agregadas.push(m.id);
    }
    // solo cuentan las que siguen en el buzón (un /borrar en la misma revisión pudo quitar alguna)
    const nuevas = agregadas.filter(id => buzon.some(c => c.id === id)).length;
    if (cambios) { guardarSetCorto('dallanaCartasBorradas', cartasBorradas); guardarSetCorto('dallanaComandosHechos', comandosHechos); }
    if (!agregadas.length && !cambios) return;
    buzon.sort((x, y) => x.t - y.t);
    guardarBuzon();
    pintarSobre();
    if (nuevas) notificar(`recibió ${nuevas === 1 ? 'tu carta' : nuevas + ' cartas tuyas'} en el buzón de Alejandro 📬`, 'mailbox_with_mail');
    if ((nuevas || hayNueva) && cartaPendiente()) avisarCartaNueva();
  } catch {}
}

/* Cuando llega una carta: la bandera del buzón sube, Alejandro camina al buzón, saca el sobre y te lo trae */
function avisarCartaNueva() {
  const globo = $('alejandroGlobo');
  if (globo && !globo.hidden) return;
  const decir = () => {
    alejandroReacciona('saludar', 2400);
    alejandroDice('¡Mamá! Llegó una carta de papá y te la traje. 💌 Tócame o toca el buzón para abrirla.', 'Alejandro cartero 🦀',
      () => { const c = cartaPendiente(); if (c) abrirCartaPapa(c); }, true);
  };
  const caja = cajaEnCasa(), bz = $('buzonEsquina');
  if (sinMovimiento() || !caja || !bz || document.visibilityState !== 'visible' || estadoPorHora() === 'dormir') { decir(); return; }
  cancelarPaseo();
  const id = paseoId;
  const sobre = $('alejandroSobre'); if (sobre) sobre.hidden = true;
  const r = bz.getBoundingClientRect();
  alejandroAlerta();
  volverACasa(() => setTimeout(() => {
    // sale corriendo al buzón (más rápido que en un paseo), saca la carta y vuelve
    caminarA({ x: r.left + r.width * .4 - caja.right, y: 0 }, false, 210).then(ok => {
      if (!ok) { pintarSobre(); return; }
      alejandroReacciona('enamorado', 1100);
      setTimeout(() => { pintarSobre(); caminarA({ x: 0, y: 0 }, false, 210).then(() => decir()); }, 1100);
    });
  }, 650), true);
}

function mostrarVistaCarta(c) {
  $('cartaPapaVista').hidden = false;
  $('buzonVista').hidden = true;
  const deMi = c.de === 'yo';
  $('cartaPapaDe').textContent = deMi ? '💌 Lo que le dijiste a papá' : '💌 Alejandro te trajo una carta';
  $('cartaPapaTitulo').textContent = deMi ? 'Para papá' : (c.titulo || 'Carta de papá');
  $('cartaPapaFecha').textContent = fechaCarta(c.t) + (c.editada ? ' · corregida ✏️' : '');
  escribirCartaSola($('cartaPapaTexto'), c.texto, !deMi);
  $('cartaResponder').hidden = deMi;
}

function abrirCartaPapa(c) {
  const dlg = $('cartaPapaDialog'); if (!dlg || !c) return;
  cerrarAlejandro(false);
  mostrarVistaCarta(c);
  if (!dlg.open) dlg.showModal();
  if (c.de === 'papa' && !c.leida) {
    c.leida = true;
    guardarBuzon();
    pintarSobre();
    notificar(`abrió tu carta 💌: «${c.texto.slice(0, 80)}${c.texto.length > 80 ? '…' : ''}»`, 'love_letter', 'Carta leida');
  }
}

function abrirBuzon() {
  const dlg = $('cartaPapaDialog'); if (!dlg) return;
  cerrarAlejandro(false);
  $('cartaPapaVista').hidden = true;
  $('buzonVista').hidden = false;
  const lista = $('buzonLista');
  lista.replaceChildren();
  [...buzon].reverse().forEach(c => {
    const li = document.createElement('li');
    const b = document.createElement('button');
    b.type = 'button';
    if (c.de === 'yo') b.classList.add('mia');
    if (c.de === 'papa' && !c.leida) b.classList.add('nueva');
    const de = document.createElement('small');
    de.textContent = `${c.de === 'yo' ? 'Tú para papá' : 'De papá'} · ${fechaCarta(c.t)}`;
    const txt = document.createElement('span');
    txt.textContent = c.texto.length > 90 ? c.texto.slice(0, 90) + '…' : c.texto;
    b.append(de, txt);
    b.onclick = () => abrirCartaPapa(c);
    li.append(b);
    lista.append(li);
  });
  $('buzonVacio').hidden = buzon.length > 0;
  if (!dlg.open) dlg.showModal();
}

function abrirParaPapa() {
  const dlg = $('paraPapaDialog'); if (!dlg) return;
  cerrarAlejandro(false);
  $('cartaPapaDialog')?.open && $('cartaPapaDialog').close();
  $('paraPapaEstado').textContent = '';
  if (!dlg.open) dlg.showModal();
  setTimeout(() => $('paraPapaTexto')?.focus(), 60);
}

$('paraPapaTexto')?.addEventListener('input', e => {
  const c = $('paraPapaCuenta'); if (c) c.textContent = `${e.target.value.length} / 600`;
});

$('paraPapaForm')?.addEventListener('submit', async e => {
  e.preventDefault();
  const ta = $('paraPapaTexto'), btn = $('paraPapaEnviar'), estado = $('paraPapaEstado');
  const texto = (ta?.value || '').trim();
  if (!texto) return;
  btn.disabled = true;
  estado.textContent = 'Alejandro va corriendo donde papá… 🦀💨';
  try {
    if (URL_RINCON) {
      await rincon('/api/aviso', { method: 'POST', body: JSON.stringify({ titulo: 'Mensaje de Dallana 💌', texto, tags: 'love_letter,crab' }) });
    } else {
      const r = await fetch('https://ntfy.sh/', {
        method: 'POST',
        body: JSON.stringify({ topic: NTFY_TEMA, title: 'Mensaje de Dallana 💌', message: texto, tags: ['love_letter', 'crab'], priority: 4 })
      });
      if (!r.ok) throw new Error(String(r.status));
    }
    buzon.push({ id: `yo-${Date.now()}`, de: 'yo', t: Date.now(), texto, leida: true });
    guardarBuzon();
    ta.value = '';
    $('paraPapaCuenta').textContent = '0 / 600';
    const desde = $('paraPapaForm').getBoundingClientRect();
    $('paraPapaDialog').close();
    entregarMensajeAPapa(desde);
  } catch {
    estado.textContent = 'Ups, no pude llegar donde papá. Revisa tu internet y prueba otra vez.';
  } finally {
    btn.disabled = false;
  }
});

function abrirMenuAlejandro() {
  const globo = $('alejandroGlobo'); if (!globo) return;
  if (!enCasa()) { volverACasa(abrirMenuAlejandro, true); return; }
  modoGlobo('menu');
  pintarSobre();
  const texto = $('alejandroTexto'); if (texto) texto.textContent = '¡Hola, mamá! ¿Qué hacemos? 🦀';
  globo.hidden = false;
  $('alejandroSprite')?.setAttribute('aria-expanded', 'true');
  estadoAlejandro();
}
$('menuBuzon')?.addEventListener('click', abrirBuzon);
$('menuParaPapa')?.addEventListener('click', abrirParaPapa);
$('menuNovedades')?.addEventListener('click', () => abrirAlejandro(0));
$('cartaResponder')?.addEventListener('click', abrirParaPapa);
$('cartaVerBuzon')?.addEventListener('click', abrirBuzon);
$('buzonParaPapa')?.addEventListener('click', abrirParaPapa);

function empezarCartero() {
  if (carteroIniciado) return;
  carteroIniciado = true;
  if (URL_RINCON && !tokenRincon) setTimeout(pedirClave, 1800);
  pintarSobre();
  if (cartaPendiente()) setTimeout(avisarCartaNueva, 4000);
  setTimeout(revisarCartas, 2500);
  setInterval(revisarCartas, 60000);
  document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'visible') revisarCartas(); });
}

/* ---------- Rutinas según la hora y el día ----------
   Cada rutina se hace una vez al día (dallanaRutinas). En una fecha especial Alejandro usa ese disfraz todo el día
   (salvo de noche, que duerme con pijama) y la saluda al entrar. */
// Cumpleaños de Dallana: 12 de agosto
const CUMPLE_DALLANA = { mes: 8, dia: 12 };
const FECHAS_ALEJANDRO = [
  { mes: 2, dia: 14, disfraz: 'san-valentin', reaccion: 'enamorado', frase: () => '¡Feliz San Valentín, mamá! Papá y yo te queremos un montón. 💘' },
  { mes: 10, dia: 31, disfraz: 'fantasmita', reaccion: 'saludar', frase: () => '¡Buuu! Feliz Halloween, mamá. ¿Me das un dulce? 🎃' },
  { mes: 12, dia: 24, disfraz: 'navidad', reaccion: 'saludar', frase: () => '¡Mamá, mañana es Navidad! Le pedí al viejito pascuero que te cuide siempre. 🎄' },
  { mes: 12, dia: 25, disfraz: 'navidad', reaccion: 'enamorado', frase: () => '¡Feliz Navidad, mamá! Tú eres el mejor regalo de papá. 🎄🎁' },
  { mes: 12, dia: 31, disfraz: 'ano-nuevo', reaccion: 'saludar', frase: () => '¡Último día del año, mamá! Gracias por este año tan bonito. 🎆' },
  { mes: 1, dia: 1, disfraz: 'ano-nuevo', reaccion: 'enamorado', frase: () => '¡Feliz año nuevo, mamá! Mi propósito es quererte todavía más. 🎆' },
  { dia: Number(FECHA_INICIO.split('-')[2]), disfraz: 'cumpleanos', reaccion: 'llorar', celebrar: true,
    frase: n => `¡Feliz cumplemes, mamá! Hoy papá y tú cumplen ${n} ${n === 1 ? 'mes' : 'meses'} juntos. Me emociono… 🥹🎂` }
];
if (CUMPLE_DALLANA) FECHAS_ALEJANDRO.unshift({ ...CUMPLE_DALLANA, disfraz: 'cumpleanos', reaccion: 'llorar', celebrar: true,
  frase: () => '¡¡Feliz cumpleaños, mamá!! 🎂 Papá y yo te preparamos un día lleno de cariño. 🎉' });

function mesesJuntos(hoy = new Date()) {
  const [anio, mes, dia] = FECHA_INICIO.split('-').map(Number);
  return (hoy.getFullYear() - anio) * 12 + hoy.getMonth() - (mes - 1) - (hoy.getDate() < dia ? 1 : 0);
}

function fechaEspecialHoy() {
  const hoy = new Date(), m = hoy.getMonth() + 1, d = hoy.getDate();
  return FECHAS_ALEJANDRO.find(f => f.dia === d && (f.mes ? f.mes === m : mesesJuntos(hoy) > 0)) || null;
}
const disfrazDelDia = () => { const f = fechaEspecialHoy(); return f ? DISFRACES.find(x => x.id === f.disfraz) || null : null; };

const RUTINAS = [
  { id: 'manana', desde: 7, hasta: 12, antes: 'bostezar', reaccion: 'saludar', frases: [
    '¡Buenos días, mamá! ☀️ ¿Dormiste bien?',
    '¡Buenos días! Papá me pidió que te diera el primer abrazo del día. 🤗',
    'Despertaste… ¡y el día ya se puso más bonito, mamá! ☀️'] },
  { id: 'almuerzo', desde: 13, hasta: 15, reaccion: 'enamorado', frases: [
    'Mamá, ¿ya almorzaste? Papá dice que comas rico. 🍝',
    'Hora de almorzar, mamá. ¡No te saltes la comida! 🍱'] },
  { id: 'tarde', desde: 17, hasta: 20, reaccion: 'saludar', accion: () => abrirParaPapa(), frases: [
    '¿Cómo te fue hoy, mamá? Tócame y se lo cuento a papá. 💌',
    'Mamá, papá quiere saber cómo estuvo tu día. Tócame y le escribimos. 💌'] },
  { id: 'noche', desde: 21, hasta: 23, reaccion: 'bostezar', frases: [
    'Ya está oscurito, mamá… no te acuestes tan tarde. 🌙',
    'Mamá, antes de dormir: papá te quiere muchísimo. 🌙💗'] }
];
let rutinasHoy = leerJSON('dallanaRutinas', {});

function hacerRutina(id, decir) {
  if (rutinasHoy.fecha !== hoyLocal()) rutinasHoy = { fecha: hoyLocal(), hechas: [] };
  if (rutinasHoy.hechas.includes(id)) return;
  if (!decir()) return;
  rutinasHoy.hechas.push(id);
  guardarJSON('dallanaRutinas', rutinasHoy);
}

function revisarRutinas() {
  if (!disfracesIniciados || document.visibilityState !== 'visible' || estadoPorHora() === 'dormir' || alejandroCaminando) return;
  const especial = fechaEspecialHoy();
  if (especial) hacerRutina(`especial-${especial.disfraz}`, () => {
    const dijo = alejandroDice(especial.frase(mesesJuntos()), 'Alejandro 🦀', null, true);
    if (dijo) { alejandroReacciona(especial.reaccion, 3200); if (especial.celebrar) lanzarCelebracion(); }
    return true;   // si no pudo decirlo ahora, queda en la fila de pendientes
  });
  const h = new Date().getHours();
  const r = RUTINAS.find(x => h >= x.desde && h < x.hasta);
  if (!r) return;
  hacerRutina(r.id, () => {
    const frase = r.frases[Math.floor(Math.random() * r.frases.length)];
    if (!alejandroDice(frase, 'Alejandro 🦀', r.accion || null)) return false;
    if (r.antes) { alejandroReacciona(r.antes, 1600); setTimeout(() => alejandroReacciona(r.reaccion, 2400), 1650); }
    else alejandroReacciona(r.reaccion, 2600);
    return true;
  });
}

/* Si pasan 2 días o más sin que entre, al volver Alejandro llora de emoción; si solo dejó la pestaña un rato, la saluda */
let ultimaVez = Number(leerJSON('dallanaUltimaVez', 0)) || 0, ocultaDesde = 0;
const marcarUltimaVez = () => { if (document.visibilityState === 'visible') guardarJSON('dallanaUltimaVez', Date.now()); };
function saludoDeRegreso() {
  const dias = ultimaVez ? (Date.now() - ultimaVez) / 864e5 : 0;
  marcarUltimaVez();
  if (dias >= 2 && estadoPorHora() !== 'dormir') {
    if (alejandroDice(`¡Mamá! Te extrañé muchísimo… ${Math.floor(dias)} días sin verte. 🥺 Qué bueno que volviste.`, 'Alejandro 🦀', null, true))
      alejandroReacciona('llorar', 3400);
  }
}
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'hidden') { marcarUltimaVez(); ocultaDesde = Date.now(); return; }
  if (ocultaDesde && Date.now() - ocultaDesde > 20 * 60000 && disfracesIniciados && estadoPorHora() !== 'dormir') {
    setTimeout(() => { if (alejandroDice('¡Volviste, mamá! Te estaba esperando. 🦀', 'Alejandro 🦀')) alejandroReacciona('saludar', 2200); }, 1200);
  }
  ocultaDesde = 0;
  setTimeout(revisarRutinas, 4000);
});

/* Reacciones a lo que hace Dallana */
// Muchos toques seguidos: se enoja de mentirita
let toquesAlejandro = [];
$('alejandroSprite')?.addEventListener('pointerdown', () => {
  const ahora = Date.now();
  toquesAlejandro = toquesAlejandro.filter(t => ahora - t < 2500).concat(ahora);
  if (toquesAlejandro.length < 6) return;
  toquesAlejandro = [];
  alejandroIgnorarClick = true;
  setTimeout(() => { alejandroIgnorarClick = false; }, 600);
  cerrarAlejandro(false);
  alejandroReacciona('enojado', 2400);
  setTimeout(() => alejandroDice('¡Mamá, me haces cosquillas! 😤 …ya, ya, te perdono. 💗', 'Alejandro 🦀'), 300);
});
// Scroll muy rápido: se marea (como mucho una vez cada 5 minutos)
(() => {
  let ultimoY = scrollY, ultimoT = performance.now(), mareoListo = 0, mareoTimer = 0;
  addEventListener('scroll', () => {
    const t = performance.now(), v = Math.abs(scrollY - ultimoY) / Math.max(1, t - ultimoT);
    ultimoY = scrollY; ultimoT = t;
    if (v < 7 || Date.now() < mareoListo || !disfracesIniciados || sinMovimiento() || estadoPorHora() === 'dormir') return;
    mareoListo = Date.now() + 300000;
    clearTimeout(mareoTimer);
    mareoTimer = setTimeout(() => {
      if (!enCasa() || alejandroCaminando) return;
      alejandroReacciona('mareado', 2600);
      alejandroDice('Uyy… tan rápido me mareé, mamá. 😵‍💫', 'Alejandro 🦀');
    }, 1500);
  }, { passive: true });
})();
// La carta principal: si la lee con calma, Alejandro se emociona
(() => {
  const dlg = $('letterDialog'); if (!dlg) return;
  let abiertaDesde = 0;
  new MutationObserver(() => { if (dlg.open) abiertaDesde = Date.now(); }).observe(dlg, { attributes: true, attributeFilter: ['open'] });
  dlg.addEventListener('close', () => {
    if (!abiertaDesde || Date.now() - abiertaDesde < 30000) return;
    abiertaDesde = 0;
    setTimeout(() => { alejandroReacciona('llorar', 3000); alejandroDice('Ay, mamá… esa carta me hizo llorar de emoción. 🥹', 'Alejandro 🦀'); }, 1500);
  });
})();

/* Mantenerlo presionado muestra el mensaje secreto */
function mostrarSecretoAlejandro() {
  const globo = $('alejandroGlobo'); if (!globo) return;
  if (!enCasa()) { volverACasa(mostrarSecretoAlejandro, true); return; }
  const texto = $('alejandroTexto'), paso = $('alejandroPaso'), sig = $('alejandroSiguiente');
  if (texto) texto.textContent = MENSAJE_SECRETO;
  if (paso) paso.textContent = '🤫 secreto';
  if (sig) sig.hidden = true;
  cancelarPaseo();
  modoGlobo('secreto');
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
   ANIMACIONES
   ============================================================ */
const animarMucho = () => !matchMedia('(prefers-reduced-motion: reduce)').matches;
const pixelSVG = (filas, colores, tam = 1) => {
  const alto = filas.length, ancho = filas[0].length;
  let r = '';
  filas.forEach((f, y) => [...f].forEach((ch, x) => { if (ch !== '.') r += `<rect x="${x}" y="${y}" width="1.02" height="1.02" fill="${colores[ch]}"/>`; }));
  return `<svg viewBox="0 0 ${ancho} ${alto}" shape-rendering="crispEdges" aria-hidden="true">${r}</svg>`;
};
const CORAZON_PIXEL = ['.oo.oo.', 'orrorro', 'orrrrro', '.orrro.', '..oro..', '...o...'];
const corazonPixel = (relleno, borde = '#8d1f2e') => pixelSVG(CORAZON_PIXEL, { o: borde, r: relleno });

/* 1. Alejandro sale del sobre de la portada y corre a su esquina */
function entradaAlejandro(rect) {
  subirAlejandro();
  const a = $('alejandro'), spr = $('alejandroSprite');
  const caja = cajaEnCasa();
  if (!a || !spr || !caja || !rect || !animarMucho()) return Promise.resolve();
  const cx = rect.left + rect.width / 2, cy = rect.top + rect.height * .45;
  const x = cx - (caja.left + caja.right) / 2, y = cy - (caja.top + caja.bottom) / 2;
  a.style.transition = 'none';
  a.style.translate = `${x}px ${y}px`;
  alejandroPos = { x, y };
  spr.classList.add('sale-sobre');
  alejandroReacciona('aplaudir', 1300);
  return new Promise(res => setTimeout(() => {
    spr.classList.remove('sale-sobre');
    caminarA({ x: 0, y: 0 }, false, 260).then(() => {
      let vista = '';
      try { vista = localStorage.getItem('dallanaNovedades') || ''; } catch {}
      if (vista === NOVEDADES.version && !tutorialPendiente()) alejandroDice('¡Hola, mamá! Te estaba esperando. 🦀💗', 'Alejandro 🦀');
      res();
    });
  }, 1300));
}

/* 2. La onda del reproductor sigue el sonido real y salen notitas pixel del vinilo.
   En iPhone/iPad no se conecta el análisis de audio (cortaría la música con la pantalla bloqueada). */
const esIOS = /iP(hone|ad|od)/.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
// Solo en PC (mouse, sin pantalla táctil): en teléfonos el sistema puede pausar el audio analizado al bloquear la pantalla
const usarAudioReal = !esIOS && matchMedia('(pointer: fine)').matches && !matchMedia('(any-pointer: coarse)').matches;
let analizador = null, datosAudio = null, visualizando = false, notaTimer = 0;
const NOTA_PIXEL = ['..oo', '..oo', '..o.', '..o.', 'ooo.', 'ooo.'];

function iniciarVisualizador() {
  const player = document.querySelector('.music-player');
  if (!player || !musicAudio || !animarMucho()) return;
  if (usarAudioReal && !analizador) {
    try {
      const Ctx = window.AudioContext || window.webkitAudioContext;
      const ctx = new Ctx();
      // conectar el audio al analizador es irreversible: solo si el sistema de audio está corriendo (si no, la música quedaría muda)
      if (ctx.state !== 'running') { ctx.close(); throw new Error('audio suspendido'); }
      const fuente = ctx.createMediaElementSource(musicAudio);
      analizador = ctx.createAnalyser();
      analizador.fftSize = 256;
      analizador.smoothingTimeConstant = .78;
      fuente.connect(analizador); analizador.connect(ctx.destination);
      datosAudio = new Uint8Array(analizador.frequencyBinCount);
      analizador._ctx = ctx;
    } catch { analizador = null; }
  }
  if (analizador && analizador._ctx.state === 'suspended') analizador._ctx.resume().catch(() => {});
  if (analizador) player.classList.add('en-vivo');
  if (!visualizando) { visualizando = true; requestAnimationFrame(cuadroVisualizador); }
  clearInterval(notaTimer);
  notaTimer = setInterval(soltarNota, 900);
}

function cuadroVisualizador() {
  if (!musicAudio || musicAudio.paused) { visualizando = false; detenerVisualizador(); return; }
  if (analizador && musicWave && document.visibilityState === 'visible') {
    analizador.getByteFrequencyData(datosAudio);
    const barras = musicWave.children, n = barras.length, utiles = Math.floor(datosAudio.length * .72);
    for (let i = 0; i < n; i++) {
      const desde = Math.floor(Math.pow(i / n, 1.6) * utiles), hasta = Math.max(desde + 1, Math.floor(Math.pow((i + 1) / n, 1.6) * utiles));
      let suma = 0; for (let k = desde; k < hasta; k++) suma += datosAudio[k];
      barras[i].style.setProperty('--nivel', ((suma / (hasta - desde)) / 255).toFixed(3));
    }
  }
  requestAnimationFrame(cuadroVisualizador);
}

function detenerVisualizador() {
  clearInterval(notaTimer);
  document.querySelector('.music-player')?.classList.remove('en-vivo');
}

function soltarNota() {
  if (!musicAudio || musicAudio.paused || document.visibilityState !== 'visible') return;
  const escena = document.querySelector('.album-stage'); if (!escena) return;
  if (escena.querySelectorAll('.nota-musica').length > 6) return;
  const n = document.createElement('span');
  n.className = 'nota-musica';
  const col = ['#d1343f', '#3d72c4', '#4f9a4a', '#ff7a6b'][Math.floor(Math.random() * 4)];
  n.innerHTML = pixelSVG(NOTA_PIXEL, { o: col });
  n.style.setProperty('--x', `${20 + Math.random() * 30}%`);
  n.style.setProperty('--y', `${30 + Math.random() * 30}%`);
  n.style.setProperty('--dx', `${-20 + Math.random() * 40}px`);
  n.style.setProperty('--rot', `${-20 + Math.random() * 40}deg`);
  escena.append(n);
  setTimeout(() => n.remove(), 2500);
}
if (musicAudio) {
  musicAudio.addEventListener('play', iniciarVisualizador);
  musicAudio.addEventListener('pause', detenerVisualizador);
}

/* 3. Chispitas cuando se llena un corazón y corazón gigante al completar los 10 */
function chispasCorazon(c) {
  if (!animarMucho()) return;
  const colores = ['#e0303f', '#f2c14e', '#ff7a6b', '#3d72c4'];
  for (let k = 0; k < 7; k++) {
    const ch = document.createElement('i');
    ch.className = 'ph-chispa';
    const ang = (k / 7) * Math.PI * 2, dist = 16 + Math.random() * 10;
    ch.style.setProperty('--dx', `${Math.cos(ang) * dist}px`);
    ch.style.setProperty('--dy', `${Math.sin(ang) * dist}px`);
    ch.style.setProperty('--c', colores[k % colores.length]);
    c.append(ch);
    setTimeout(() => ch.remove(), 650);
  }
}

const CORAZON_GRANDE = ['.ooo.ooo.', 'orrrorrro', 'orwrrrrro', 'orrrrrrro', '.orrrrro.', '..orrro..', '...oro...', '....o....'];
function corazonGigante() {
  if (!animarMucho()) return;
  const caja = $('progressHearts');
  const cx = innerWidth / 2, cy = innerHeight / 2;
  if (caja) [...caja.children].forEach((c, i) => {
    const r = c.getBoundingClientRect();
    if (r.bottom < 0 || r.top > innerHeight) return;
    const v = document.createElement('span');
    v.className = 'corazon-viajero';
    v.innerHTML = SVG_CORAZON;
    v.style.left = `${r.left}px`; v.style.top = `${r.top}px`;
    document.body.append(v);
    v.animate([{ transform: 'translate(0,0) scale(1)', opacity: 1 },
               { transform: `translate(${cx - r.left - 14}px, ${cy - r.top - 13}px) scale(.6)`, opacity: .9 }],
              { duration: 650, delay: i * 45, easing: 'cubic-bezier(.5,0,.6,1)', fill: 'forwards' }).onfinish = () => v.remove();
    setTimeout(() => v.remove(), 1500);
  });
  setTimeout(() => {
    const g = document.createElement('div');
    g.className = 'corazon-gigante';
    g.innerHTML = pixelSVG(CORAZON_GRANDE, { o: '#8d1f2e', r: '#e0303f', w: '#ffb3b8' });
    document.body.append(g);
    setTimeout(() => g.remove(), 2700);
  }, 950);
}

/* 4. El recuerdo pixel se revela como una foto instantánea */
function revelarRecuerdo() {
  const m = $('pixelMarco'); if (!m || !animarMucho()) return;
  m.classList.remove('revelando'); void m.offsetWidth; m.classList.add('revelando');
  setTimeout(() => m.classList.remove('revelando'), 2800);
}

/* 5. El sello de cera se parte en pedacitos al abrir una carta «Ábreme cuando» */
function romperSello(scene) {
  const sello = scene.querySelector('.envelope-seal');
  if (!sello || !animarMucho()) return;
  const rs = sello.getBoundingClientRect(), re = scene.getBoundingClientRect();
  const x = rs.left - re.left + rs.width / 2, y = rs.top - re.top + rs.height / 2;
  scene.classList.add('rompe-sello');
  const destello = document.createElement('span');
  destello.className = 'sello-destello';
  destello.style.left = `${x - 30}px`; destello.style.top = `${y - 30}px`;
  scene.append(destello);
  setTimeout(() => destello.remove(), 500);
  for (let k = 0; k < 8; k++) {
    const t = document.createElement('span');
    t.className = 'sello-trozo';
    const w = 8 + Math.random() * 10, h = 7 + Math.random() * 9;
    t.style.setProperty('--w', `${w}px`); t.style.setProperty('--h', `${h}px`);
    t.style.left = `${x - w / 2 + (Math.random() * 16 - 8)}px`; t.style.top = `${y - h / 2 + (Math.random() * 16 - 8)}px`;
    const ang = -Math.PI / 2 + (Math.random() - .5) * Math.PI * 1.4;
    t.style.setProperty('--dx', `${Math.cos(ang) * (40 + Math.random() * 50)}px`);
    t.style.setProperty('--dy', `${120 + Math.random() * 90}px`);
    t.style.setProperty('--rot', `${Math.random() * 540 - 270}deg`);
    t.style.clipPath = `polygon(${Math.random() * 30}% 0, 100% ${Math.random() * 40}%, ${70 + Math.random() * 30}% 100%, 0 ${50 + Math.random() * 50}%)`;
    scene.append(t);
    setTimeout(() => t.remove(), 950);
  }
}

/* 6. La carta de papá se escribe sola, letra por letra, con una plumita (toca la carta para verla entera) */
let escrituraId = 0;
const PLUMA_SVG = pixelSVG(['......oo', '.....owo', '....owo.', '...owo..', '..owo...', '.oo.....', 'oo......', 'o.......'], { o: '#5a3a2a', w: '#fffaf2' });
function escribirCartaSola(el, texto, animar) {
  const id = ++escrituraId;
  const papel = el.closest('.carta-papa-papel');
  if (!animar || !animarMucho()) { el.textContent = texto; papel?.classList.remove('escribiendo'); return; }
  el.textContent = '';
  el.setAttribute('aria-label', texto);
  const escrito = document.createTextNode('');
  const pluma = document.createElement('span');
  pluma.className = 'pluma'; pluma.innerHTML = PLUMA_SVG;
  el.append(escrito, pluma);
  papel?.classList.add('escribiendo');
  const terminar = () => {
    if (id !== escrituraId) return;
    escrituraId++;
    el.textContent = texto; el.removeAttribute('aria-label');
    papel?.classList.remove('escribiendo');
    if (papel) papel.onclick = null;
  };
  if (papel) papel.onclick = terminar;
  const pausa = Math.max(14, Math.min(45, 5500 / Math.max(1, texto.length)));
  let i = 0;
  const paso = () => {
    if (id !== escrituraId) return;
    if (i >= texto.length) { terminar(); return; }
    const ch = texto[i++];
    escrito.data += ch;
    setTimeout(paso, /[.,!?¡¿…\n]/.test(ch) ? pausa * 6 : pausa);
  };
  setTimeout(paso, 350);
}
$('cartaPapaDialog')?.addEventListener('close', () => { escrituraId++; });

/* 7. El mensaje para papá se dobla en avioncito; Alejandro lo atrapa y corre a entregarlo */
const AVION_SVG = '<svg viewBox="0 0 44 34" aria-hidden="true"><path d="M2 16 42 2 30 32 21 21z" fill="#fffaf2" stroke="#b8222f" stroke-width="2" stroke-linejoin="round"/><path d="M42 2 21 21l-4 10 4-10" fill="#f3d9d2" stroke="#b8222f" stroke-width="2" stroke-linejoin="round"/><path d="M14 13c-2-3 1-6 4-4 2-3 6 0 4 3l-4 4z" fill="#e0303f"/></svg>';
function entregarMensajeAPapa(desde) {
  const antes = disfrazActual;
  const fin = () => {
    if (disfrazActual === DISFRAZ_CARTERO) ponerDisfraz(antes, false);
    alejandroReacciona('enamorado', 2400);
    setTimeout(() => alejandroDice('¡Entregado, mamá! Papá ya lo tiene. 💌', 'Alejandro cartero 🦀', null, true), 400);
  };
  const caja = cajaEnCasa(), a = $('alejandro');
  if (!animarMucho() || !caja || !a || !desde) { fin(); return; }
  cancelarPaseo();
  volverACasa(() => {
    const av = document.createElement('div');
    av.className = 'avioncito'; av.innerHTML = AVION_SVG;
    document.body.append(av);
    const x0 = desde.left + desde.width / 2 - 22, y0 = desde.top + desde.height / 2 - 17;
    const x1 = (caja.left + caja.right) / 2 - 22, y1 = caja.top + 10;
    const mx = (x0 + x1) / 2 + 60, my = Math.min(y0, y1) - 120;
    let llego = false;
    const alLlegar = () => {
      if (llego) return;
      llego = true;
      av.remove();
      const sobre = $('alejandroSobre'); if (sobre) sobre.hidden = false;
      ponerDisfraz(DISFRAZ_CARTERO, false);
      alejandroReacciona('saludar', 700);
      setTimeout(() => {
        // corre fuera de la pantalla con la carta… y vuelve
        const fuera = innerWidth + 60 - caja.left;
        caminarA({ x: fuera, y: 0 }, false, 340).then(() => setTimeout(() => {
          pintarSobre();
          caminarA({ x: 0, y: 0 }, false, 340).then(fin);
        }, 1400));
      }, 700);
    };
    av.animate([
      { transform: `translate(${x0}px, ${y0}px) rotate(-10deg) scale(1.3)` },
      { transform: `translate(${mx}px, ${my}px) rotate(-35deg) scale(1)`, offset: .45 },
      { transform: `translate(${x1}px, ${y1}px) rotate(15deg) scale(.6)` }
    ], { duration: 1300, easing: 'ease-in-out', fill: 'forwards' }).onfinish = alLlegar;
    setTimeout(alLlegar, 1700);   // respaldo si la animación se congela
  }, true);
}

/* 8. Las polaroids se mecen con el scroll */
(() => {
  if (!animarMucho()) return;
  let ultimo = scrollY, pendiente = false;
  addEventListener('scroll', () => {
    if (pendiente) return;
    pendiente = true;
    requestAnimationFrame(() => {
      pendiente = false;
      const delta = scrollY - ultimo; ultimo = scrollY;
      if (Math.abs(delta) < 2) return;
      document.querySelectorAll('.photo-card').forEach((c, i) => {
        const r = c.getBoundingClientRect();
        if (r.bottom < 0 || r.top > innerHeight) return;
        const f = [1, -.8, 1.2, -1][i % 4];
        c.style.setProperty('--mecer', Math.max(-5, Math.min(5, delta * .12 * f)).toFixed(2));
        clearTimeout(c._mecer);
        c._mecer = setTimeout(() => c.style.setProperty('--mecer', '0'), 120);
      });
    });
  }, { passive: true });
})();

/* 9. Cielo detrás de la página: un cielo pastel de día (celeste arriba, durazno y rosa abajo) y uno de noche
   (azul tinta a rosa del atardecer), con nubes pixel en tres capas que pasan lento, estrellas de noche
   y dragoncitos de colores que cruzan volando de vez en cuando (detrás de las secciones, nunca encima).
   Noche visual: de 20 a 6 h, igual que la portada y la postal. Dragones: propuesta/dragones.py. */
const NUBE_PIXEL = ['....oooo........', '..oowwwwoo.oooo..', '.owwwwwwwwowwwwo.', 'owwwwwwwwwwwwwwwo', 'owwwwwwwwwwwwwwwo', '.ooooooooooooooo.'];
const NUBES = [
  NUBE_PIXEL,
  ['......ooo......', '....oowwwoo....', '..oowwwwwwwoo..', '.owwwwwwwwwwwo.', 'owwwwwwwwwwwwwo', '.ooooooooooooo.'],
  ['...ooo.....ooo....', '.oowwwoo.oowwwoo..', 'owwwwwwwowwwwwwwo.', 'owwwwwwwwwwwwwwwwo', '.oooooooooooooooo.']
];
let fugazTimer = 0, cieloEraNoche = null;
const nocheVisual = () => { const h = new Date().getHours(); return h >= 20 || h < 6; };

function pintarCielo() {
  const cielo = $('cielo'); if (!cielo) return;
  const noche = nocheVisual();
  cieloEraNoche = noche;
  document.body.classList.toggle('noche-visual', noche);
  cielo.classList.toggle('noche', noche);
  cielo.querySelectorAll('.nube,.estrella,.fugaz').forEach(e => e.remove());   // los dragones que van volando siguen
  clearInterval(fugazTimer);
  const chico = innerWidth < 600;
  if (noche) {
    const cols = ['#ffe7a3', '#ffe7a3', '#ffc2cc', '#bcd3ff'];
    for (let k = 0, n = chico ? 24 : 44; k < n; k++) {
      const e = document.createElement('i');
      e.className = 'estrella';
      e.style.left = `${Math.random() * 100}%`; e.style.top = `${Math.random() * 78}%`;
      e.style.setProperty('--t', `${Math.random() < .2 ? 4 : 3}px`);
      e.style.setProperty('--c', cols[k % cols.length]);
      e.style.setProperty('--d', `${2 + Math.random() * 3}s`);
      e.style.setProperty('--r', `${-Math.random() * 4}s`);
      cielo.append(e);
    }
    if (animarMucho()) fugazTimer = setInterval(() => {
      if (document.visibilityState !== 'visible') return;
      const f = document.createElement('i');
      f.className = 'fugaz';
      f.style.left = `${40 + Math.random() * 60}%`; f.style.top = `${Math.random() * 40}%`;
      cielo.append(f);
      setTimeout(() => f.remove(), 1400);
    }, 14000);
  }
  // nubes en tres capas: lejos (chicas, lentas y suaves), al medio y cerca (grandes y más rápidas)
  const capas = [['lejos', chico ? 2 : 3, 60, 90, 170], ['medio', chico ? 2 : 3, 100, 140, 120], ['cerca', chico ? 1 : 2, 150, 210, 85]];
  const colores = noche ? { o: '#6a64a8', w: '#9a92d0' } : { o: '#c9d9f0', w: '#ffffff' };
  capas.forEach(([capa, n, wMin, wMax, dur]) => {
    for (let k = 0; k < n; k++) {
      const forma = NUBES[Math.floor(Math.random() * NUBES.length)];
      const largo = Math.max(...forma.map(f => f.length));
      const nb = document.createElement('i');
      nb.className = `nube nube--${capa}`;
      nb.innerHTML = pixelSVG(forma.map(f => f.padEnd(largo, '.')), colores);
      nb.style.setProperty('--y', `${3 + Math.random() * 82}%`);
      const w = wMin + Math.random() * (wMax - wMin);
      nb.style.setProperty('--w', `${chico ? w * .7 : w}px`);
      nb.style.setProperty('--h', `${(forma.length / largo).toFixed(3)}`);
      const d = dur * (.85 + Math.random() * .3);
      nb.style.setProperty('--d', `${d}s`);
      nb.style.setProperty('--r', `${-Math.random() * d}s`);
      cielo.append(nb);
    }
  });
}
// a las 20 y a las 6 cambia el cielo
setInterval(() => { if (nocheVisual() !== cieloEraNoche) pintarCielo(); }, 60000);

/* Dragoncitos que cruzan el cielo: 10 formas y colores, a distintas distancias (los lejanos más chicos y lentos) */
const DRAGONES_TOTAL = 10;   // columnas de assets/pixel/dragones.png
let dragonesVolando = 0;
/* En el teléfono las secciones tapan casi todo el cielo: busca un hueco libre entre dos secciones
   que esté en pantalla (al menos 40 px de alto) para que el dragón pase justo por ahí. */
function huecoDeCielo() {
  const bloques = [...document.querySelectorAll('main>section,main>header,.page-footer')]
    .map(e => e.getBoundingClientRect()).filter(r => r.height && r.bottom > 0 && r.top < innerHeight)
    .sort((x, y) => x.top - y.top);
  const huecos = [];
  let desde = 0;
  bloques.forEach(r => { if (r.top - desde >= 40) huecos.push([desde, r.top]); desde = Math.max(desde, r.bottom); });
  if (innerHeight - desde >= 40) huecos.push([desde, innerHeight]);
  const buenos = huecos.map(([a, b]) => [Math.max(a, 8), Math.min(b, innerHeight - 8)]).filter(([a, b]) => b - a >= 40);
  return buenos.length ? buenos[Math.floor(Math.random() * buenos.length)] : null;
}
function soltarDragon() {
  const cielo = $('cielo');
  const chico = innerWidth < 600;
  let reintento = false;
  if (cielo && animarMucho() && document.visibilityState === 'visible' && dragonesVolando < 2) {
    const r = Math.random();
    let [capa, escala, dur] = r < .35 ? ['lejos', 1.1, 36] : r < .75 ? ['medio', 1.6, 27] : ['cerca', 2.2, 20];
    let top = `${6 + Math.random() * 74}%`;
    if (chico) {
      const hueco = huecoDeCielo();
      if (!hueco) reintento = true;
      else {
        // tan grande como quepa en el hueco, nítido y rápido para que alcance a verse entero
        const alto = hueco[1] - hueco[0];
        // las alas pueden asomar detrás de las tarjetas, como si pasara entre dos páginas
        escala = Math.max(1, Math.min(1.7, alto * 1.15 / 48));
        capa = 'cerca'; dur = 6 + Math.random() * 2;
        top = `${Math.round(hueco[0] + (alto - 48 * escala) / 2)}px`;
      }
    }
    if (!reintento) {
    const el = document.createElement('i');
    el.className = `dragon dragon--${capa}${Math.random() < .5 ? ' al-reves' : ''}${chico ? ' en-hueco' : ''}`;
    el.style.setProperty('--n', Math.floor(Math.random() * DRAGONES_TOTAL));
    el.style.setProperty('--e', escala);
    el.style.setProperty('--dur', `${chico ? dur : dur * (.9 + Math.random() * .2)}s`);
    el.style.top = top;
    const cuerpo = document.createElement('span');
    cuerpo.className = 'dragon-cuerpo';
    el.append(cuerpo);
    cielo.append(el);
    dragonesVolando++;
    let fuera = false;
    const quitar = () => { if (fuera) return; fuera = true; el.remove(); dragonesVolando--; };
    el.addEventListener('animationend', e => { if (e.target === el) quitar(); });
    setTimeout(quitar, dur * 1300 + 1000);   // respaldo si la animación se congela
    }
  }
  // en el teléfono salen más seguido (y si no había hueco, vuelve a mirar en un ratito)
  setTimeout(soltarDragon, reintento ? 2500 : chico ? 7000 + Math.random() * 9000 : 12000 + Math.random() * 22000);
}
setTimeout(soltarDragon, 3500);

/* 10. Las secciones entran como páginas de álbum que se pegan con cinta */
(() => {
  if (!animarMucho() || !('IntersectionObserver' in window)) return;
  // incluye las que todavía están ocultas (el museo aparece después de cargar el contenido) para que también lleven su cinta
  const paginas = document.querySelectorAll('main>section,main>header');
  const pegar = el => {
    if (!el.classList.contains('por-pegar')) return;
    obs.unobserve(el);
    el.classList.remove('por-pegar');
    el.classList.add('pegada');
    setTimeout(() => el.classList.remove('pegada'), 1300);
  };
  const obs = new IntersectionObserver(entradas => entradas.forEach(en => { if (en.isIntersecting) pegar(en.target); }),
    { threshold: 0, rootMargin: '0px 0px -8% 0px' });
  // respaldo por si el observador no avisa (navegadores antiguos): al hacer scroll se muestran las que ya están en pantalla
  let revisando = false;
  const revisar = () => {
    revisando = false;
    document.querySelectorAll('main>.por-pegar').forEach(el => { if (el.getBoundingClientRect().top < innerHeight * .95) pegar(el); });
  };
  ['scroll', 'resize'].forEach(ev => addEventListener(ev, () => { if (!revisando) { revisando = true; setTimeout(revisar, 150); } }, { passive: true }));
  setTimeout(revisar, 2500);
  paginas.forEach((el, i) => {
    if (i > 0) {
      const cinta = document.createElement('span');
      cinta.className = 'cinta-album'; cinta.setAttribute('aria-hidden', 'true');
      cinta.style.background = ['rgba(240,150,140,.55)', 'rgba(170,200,240,.6)', 'rgba(242,193,78,.5)', 'rgba(160,210,150,.55)'][i % 4];
      el.append(cinta);
    }
    el.classList.add('por-pegar');
    obs.observe(el);
  });
})();

/* 11. Corazoncitos pixel donde tocas la pantalla */
(() => {
  if (!animarMucho()) return;
  let ultimo = 0;
  const cols = ['#e0303f', '#ff7a6b', '#f2a0b4', '#d1343f'];
  // sale solo con un toque o clic (no al deslizar para hacer scroll en el teléfono)
  let inicio = null;
  document.addEventListener('pointerdown', e => { inicio = { x: e.clientX, y: e.clientY, t: performance.now() }; }, { passive: true });
  document.addEventListener('pointerup', e => {
    if (!inicio || Math.hypot(e.clientX - inicio.x, e.clientY - inicio.y) > 10 || performance.now() - inicio.t > 600) return;
    inicio = null;
    if (e.target.closest('input, textarea, select, .waveform, .music-volume')) return;
    const ahora = performance.now();
    if (ahora - ultimo < 110) return;
    ultimo = ahora;
    const h = document.createElement('span');
    h.className = 'toque-corazon';
    h.innerHTML = corazonPixel(cols[Math.floor(Math.random() * cols.length)]);
    h.style.left = `${e.clientX}px`; h.style.top = `${e.clientY}px`;
    document.body.append(h);
    setTimeout(() => h.remove(), 950);
  }, { passive: true });
})();

pintarCielo();

/* ============================================================
   MINI-JUEGO: Alejandro atrapa corazones (con el disfraz que tenga puesto)
   - Corazón +1 · dorado +5 · carta +3 (y una frase) · estrella = imán 6 s · burbuja = escudo contra una nube
   - Nubecitas de lluvia quitan una vida (3). Racha: x2 desde 10 seguidos, x3 desde 25.
   - Cada 30 puntos sube de nivel (más rápido). Cielo según la hora. Se pausa si sale de la pestaña.
   - Récord en dallanaRecordJuego (si lo supera, papá recibe el aviso). Con 20+ puntos llena un corazón del día (una vez al día).
   ============================================================ */
(() => {
  const dlg = $('juegoDialog'), cv = $('juegoCanvas');
  if (!dlg || !cv) return;
  const ctx = cv.getContext('2d');
  ctx.imageSmoothingEnabled = false;
  const W = cv.width, H = cv.height;
  const CEL = 72, ALTO = 86, ESC = 1.26;      // celdas de la hoja de Alejandro y su tamaño en el juego
  const FILA = { quieto: 0, aplaudir: 1, bailar: 2, caminar: 5, enamorado: 8, mareado: 10 };
  const BOCA = H - 70;                         // altura donde Alejandro atrapa
  const PIXEL = {
    corazon: ['.oo.oo.', 'orrorro', 'orrrrro', '.orrro.', '..oro..', '...o...'],
    nube: ['..oooo....', '.owwwwo.oo', 'owwwwwwowwo', 'owwwwwwwwwo', '.ooooooooo.'],
    carta: ['oooooooo', 'owwwwwwo', 'oowwwwoo', 'owowwowo', 'owwrrwwo', 'oooooooo'],
    estrella: ['...o...', '..oyo..', 'ooyyyoo', 'oyyyyyo', '.oyyyo.', '.oyoyo.', 'oo...oo']
  };
  const FRASES_CARTA = ['Te quiero mucho 💗', 'Eres mi lugar favorito', 'Te elijo siempre', '¡Qué linda eres!', 'Mi persona favorita', 'Gracias por existir', 'Contigo todo es mejor'];
  const MEDALLAS = [[100, '💎', 'diamante'], [60, '🥇', 'oro'], [30, '🥈', 'plata'], [10, '🥉', 'bronce']];
  const fuente = (getComputedStyle(document.documentElement).getPropertyValue('--firma') || 'cursive').trim();

  let hoja = null, estado = 'menu', puntos = 0, vidas = 3, cosas = [], chispas = [], textos = [];
  let ultimo = 0, proxima = 0, racha = 0, mejorRacha = 0, nivel = 1, atrapados = 0;
  let iman = 0, escudo = false, invulnerable = 0, mareo = 0, baile = 0, sacudida = 0, banner = null, cuentaHasta = 0;
  let ale = { x: W / 2, destino: W / 2, atrapa: 0 };
  let nubesFondo = [];
  const leerRecord = () => Number(leerJSON('dallanaRecordJuego', 0)) || 0;
  const multiplicador = () => racha >= 25 ? 3 : racha >= 10 ? 2 : 1;

  /* --- sonidos chiquitos (WebAudio), se pueden apagar --- */
  let audio = null;
  let sonido = leerJSON('dallanaJuegoSonido', true) !== false;
  function tono(f, dur = .07, tipo = 'square', vol = .035, f2 = null) {
    if (!sonido) return;
    try {
      audio = audio || new (window.AudioContext || window.webkitAudioContext)();
      const o = audio.createOscillator(), g = audio.createGain(), t = audio.currentTime;
      o.type = tipo; o.frequency.setValueAtTime(f, t);
      if (f2) o.frequency.exponentialRampToValueAtTime(f2, t + dur);
      g.gain.setValueAtTime(vol, t); g.gain.exponentialRampToValueAtTime(.0001, t + dur);
      o.connect(g).connect(audio.destination); o.start(t); o.stop(t + dur + .02);
    } catch {}
  }
  const arpegio = (notas, sep = 70) => notas.forEach((n, i) => setTimeout(() => tono(n, .09), i * sep));
  function pintarSonido() {
    const b = $('juegoSonido'); if (!b) return;
    b.textContent = sonido ? '🔊' : '🔇';
    b.setAttribute('aria-label', sonido ? 'Silenciar sonidos del juego' : 'Activar sonidos del juego');
  }

  function pintarRecord() {
    const r = leerRecord();
    $('juegoRecord').textContent = r;
    const t = $('juegoRecordTxt'); if (t) t.textContent = r ? `· récord ${r}` : '';
  }
  function pintarVidas() {
    const v = Math.max(0, vidas);
    $('juegoVidas').textContent = '❤️'.repeat(v) + '🤍'.repeat(3 - v) + (escudo ? ' 🛡️' : '');
  }
  function pintarPuntos() {
    $('juegoPuntos').textContent = puntos;
    const m = multiplicador(), c = $('juegoRacha');
    if (c) { c.textContent = m > 1 ? `x${m}` : ''; c.hidden = m === 1; }
  }

  function dibujarPixel(filas, colores, x, y, t) {
    filas.forEach((f, j) => [...f].forEach((ch, i) => {
      if (ch === '.') return;
      ctx.fillStyle = colores[ch];
      ctx.fillRect(Math.round(x + i * t), Math.round(y + j * t), Math.ceil(t), Math.ceil(t));
    }));
  }

  /* --- cielo según la hora, cerros y nubes lejanas --- */
  function momento() {
    const h = new Date().getHours();
    return h >= 20 || h < 7 ? 'noche' : h < 12 ? 'manana' : 'tarde';
  }
  const CIELOS = {
    manana: { cielo: ['#cfe8ff', '#fde7ef'], cerro: ['#b5dcae', '#97cb8e'], pasto: ['#bfe3b0', '#9ccd8c'], nube: '#ffffff' },
    tarde: { cielo: ['#ffd3b5', '#fff1d6'], cerro: ['#b9d79c', '#9cc581'], pasto: ['#c4e2a4', '#a3cd87'], nube: '#fff6ee' },
    noche: { cielo: ['#2b3a6b', '#6a6fa8'], cerro: ['#3f5a6e', '#33495c'], pasto: ['#4d6b62', '#3e5a52'], nube: '#9aa6d6' }
  };
  const ESTRELLAS_FONDO = Array.from({ length: 26 }, () => ({ x: Math.random() * W, y: Math.random() * H * .55, f: Math.random() * 6 }));
  function dibujarFondo(ahora) {
    const p = CIELOS[momento()];
    const g = ctx.createLinearGradient(0, 0, 0, H);
    g.addColorStop(0, p.cielo[0]); g.addColorStop(1, p.cielo[1]);
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    if (momento() === 'noche') {
      ESTRELLAS_FONDO.forEach(s => {
        ctx.globalAlpha = .45 + .55 * Math.abs(Math.sin(ahora / 700 + s.f));
        ctx.fillStyle = '#fff6c8'; ctx.fillRect(Math.round(s.x), Math.round(s.y), 2, 2);
      });
      ctx.globalAlpha = 1;
      ctx.fillStyle = '#fff6c8'; ctx.beginPath(); ctx.arc(W - 46, 46, 15, 0, 7); ctx.fill();
      ctx.fillStyle = p.cielo[0]; ctx.beginPath(); ctx.arc(W - 39, 41, 13, 0, 7); ctx.fill();
    } else {
      ctx.fillStyle = momento() === 'manana' ? '#ffe7a3' : '#ffc28a';
      ctx.beginPath(); ctx.arc(W - 48, 50, 16, 0, 7); ctx.fill();
    }
    // nubes lejanas que pasan lento
    ctx.globalAlpha = .75;
    nubesFondo.forEach(n => {
      n.x += n.v; if (n.x > W + 40) n.x = -60;
      dibujarPixel(PIXEL.nube, { o: p.nube, w: p.nube }, n.x, n.y, n.t);
    });
    ctx.globalAlpha = 1;
    // dos capas de cerros (Conce) en pixel
    [[0, H - 92, 54, .012], [1, H - 62, 38, .02]].forEach(([i, base, alto, frec]) => {
      ctx.fillStyle = p.cerro[i];
      for (let x = 0; x < W; x += 4) {
        const y = base - Math.round((Math.sin(x * frec + i * 2) * .5 + .5) * alto / 4) * 4;
        ctx.fillRect(x, y, 4, H - y);
      }
    });
    ctx.fillStyle = p.pasto[0]; ctx.fillRect(0, H - 18, W, 18);
    ctx.fillStyle = p.pasto[1];
    for (let x = 0; x < W; x += 8) ctx.fillRect(x, H - 18 + ((x / 8) % 2) * 2, 4, 2);
  }

  /* --- cosas que caen --- */
  function soltar(ahora) {
    const r = Math.random();
    const pNube = .2 + Math.min(.16, puntos / 380);
    const tipo = r < .02 ? 'estrella'
      : r < .045 && !escudo ? 'burbuja'
      : r < .09 ? 'carta'
      : r < .19 ? 'oro'
      : r < .19 + pNube ? 'nube' : 'corazon';
    const vel = 1 + (nivel - 1) * .22;
    cosas.push({ tipo, x: 22 + Math.random() * (W - 44), y: -20, v: (1.6 + Math.random() * 1.2) * vel, giro: Math.random() * 6 });
    proxima = ahora + Math.max(330, 880 - puntos * 5) * (.7 + Math.random() * .6);
  }

  function dibujarCosa(c, ahora) {
    const bam = Math.sin(ahora / 300 + c.giro) * 2;
    if (c.tipo === 'nube') {
      dibujarPixel(PIXEL.nube, { o: '#7d86b8', w: '#c9d3f2' }, c.x - 16 + bam, c.y - 8, 3);
      ctx.fillStyle = '#6fa0e8';
      for (let k = 0; k < 3; k++) ctx.fillRect(c.x - 9 + k * 9 + bam, c.y + 9 + ((ahora / 90 + k * 5) % 10), 2, 4);
    } else if (c.tipo === 'carta') {
      dibujarPixel(PIXEL.carta, { o: '#8d1f2e', w: '#fff6ea', r: '#e0303f' }, c.x - 12 + bam, c.y - 9, 3);
    } else if (c.tipo === 'estrella') {
      ctx.save(); ctx.translate(c.x + bam, c.y); ctx.rotate(Math.sin(ahora / 200) * .25);
      dibujarPixel(PIXEL.estrella, { o: '#a8781f', y: '#ffd84a' }, -10.5, -10.5, 3);
      ctx.restore();
    } else if (c.tipo === 'burbuja') {
      ctx.strokeStyle = '#6fa0e8'; ctx.lineWidth = 3; ctx.fillStyle = 'rgba(160,200,255,.35)';
      ctx.beginPath(); ctx.arc(c.x + bam, c.y, 12, 0, 7); ctx.fill(); ctx.stroke();
      ctx.fillStyle = '#fff'; ctx.fillRect(c.x + bam - 6, c.y - 7, 4, 4);
    } else {
      const oro = c.tipo === 'oro';
      dibujarPixel(PIXEL.corazon, { o: oro ? '#a8781f' : '#8d1f2e', r: oro ? '#f7c948' : '#e0303f' }, c.x - 10 + bam, c.y - 9, 3);
      if (oro) { ctx.fillStyle = '#fff6c8'; ctx.fillRect(c.x - 4 + bam, c.y - 6, 3, 3); }
    }
  }

  function chispazo(x, y, colores, n = 8) {
    for (let i = 0; i < n; i++) {
      const a = Math.random() * Math.PI * 2, s = 1 + Math.random() * 2.6;
      chispas.push({ x, y, vx: Math.cos(a) * s, vy: Math.sin(a) * s - 1.5, vida: 1, color: colores[i % colores.length] });
    }
  }
  function flotar(x, y, txt, color = '#8d1f2e', tam = 18, dur = 1400) { textos.push({ x, y, txt, color, tam, vida: 1, dur }); }

  function dibujar(ahora) {
    ctx.save();
    if (sacudida > ahora) ctx.translate((Math.random() - .5) * 8, (Math.random() - .5) * 6);
    dibujarFondo(ahora);
    cosas.forEach(c => dibujarCosa(c, ahora));
    // Alejandro
    if (hoja?.complete && hoja.naturalWidth) {
      const fila = mareo > ahora ? FILA.mareado
        : baile > ahora ? FILA.bailar
        : iman > ahora ? FILA.enamorado
        : ale.atrapa > ahora ? FILA.aplaudir
        : Math.abs(ale.destino - ale.x) > 2 ? FILA.caminar : FILA.quieto;
      const f = Math.floor(ahora / 85) % 12;
      const w = CEL * ESC, h = ALTO * ESC;
      const parpadeo = invulnerable > ahora && Math.floor(ahora / 90) % 2;
      ctx.save();
      if (parpadeo) ctx.globalAlpha = .35;
      if (ale.destino < ale.x - 2) { ctx.translate(ale.x, 0); ctx.scale(-1, 1); ctx.translate(-ale.x, 0); }
      ctx.drawImage(hoja, f * CEL, fila * ALTO, CEL, ALTO, ale.x - w / 2, H - h - 4, w, h);
      ctx.restore();
      if (escudo) {
        ctx.strokeStyle = 'rgba(111,160,232,.8)'; ctx.lineWidth = 3; ctx.fillStyle = 'rgba(160,200,255,.18)';
        ctx.beginPath(); ctx.ellipse(ale.x, H - h / 2 - 6, w * .42, h * .5, 0, 0, 7); ctx.fill(); ctx.stroke();
      }
      if (iman > ahora) {
        ctx.strokeStyle = `rgba(247,201,72,${.35 + .25 * Math.sin(ahora / 120)})`; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.arc(ale.x, BOCA, 46 + (ahora / 20) % 24, 0, 7); ctx.stroke();
      }
    }
    // chispas y textos
    chispas.forEach(p => { ctx.globalAlpha = Math.max(0, p.vida); ctx.fillStyle = p.color; ctx.fillRect(Math.round(p.x), Math.round(p.y), 3, 3); });
    ctx.globalAlpha = 1;
    ctx.textAlign = 'center';
    textos.forEach(t => {
      ctx.globalAlpha = Math.max(0, Math.min(1, t.vida * 1.6));
      ctx.font = `700 ${t.tam}px ${fuente}`;
      ctx.lineWidth = 4; ctx.strokeStyle = '#fffdf8'; ctx.strokeText(t.txt, t.x, t.y);
      ctx.fillStyle = t.color; ctx.fillText(t.txt, t.x, t.y);
    });
    ctx.globalAlpha = 1;
    // barra del imán
    if (iman > ahora) {
      const r = (iman - ahora) / 6000;
      ctx.fillStyle = 'rgba(255,253,248,.8)'; ctx.fillRect(10, 10, 84, 10);
      ctx.fillStyle = '#f7c948'; ctx.fillRect(12, 12, 80 * r, 6);
    }
    // cartel de nivel o cuenta regresiva
    const cartel = estado === 'cuenta' ? String(Math.max(1, Math.ceil((cuentaHasta - ahora) / 700))) : banner && banner.hasta > ahora ? banner.txt : '';
    if (cartel) {
      const tam = estado === 'cuenta' ? 64 : 34;
      ctx.font = `700 ${tam}px ${fuente}`;
      ctx.lineWidth = 6; ctx.strokeStyle = '#fffdf8'; ctx.strokeText(cartel, W / 2, H / 2 - 20);
      ctx.fillStyle = '#8d1f2e'; ctx.fillText(cartel, W / 2, H / 2 - 20);
    }
    ctx.restore();
  }

  function atrapar(c, ahora) {
    if (c.tipo === 'nube') {
      if (invulnerable > ahora) return;
      if (escudo) {
        escudo = false; pintarVidas();
        chispazo(c.x, c.y, ['#6fa0e8', '#c9d3f2', '#ffffff'], 12);
        flotar(c.x, c.y - 10, '¡Plop! 💦', '#3d72c4');
        tono(520, .12, 'triangle', .05, 260);
        return;
      }
      vidas--; racha = 0; pintarVidas(); pintarPuntos(); vibrar();
      mareo = ahora + 900; invulnerable = ahora + 1100; sacudida = ahora + 260;
      chispazo(c.x, c.y, ['#6fa0e8', '#7d86b8'], 10);
      tono(190, .25, 'sawtooth', .04, 90);
      if (vidas <= 0) terminar();
      return;
    }
    if (c.tipo === 'estrella') {
      iman = ahora + 6000; baile = 0;
      flotar(c.x, c.y - 10, '¡Imán de corazones! ⭐', '#a8781f', 17);
      chispazo(c.x, c.y, ['#ffd84a', '#fff6c8', '#f7c948'], 14);
      arpegio([660, 880, 1100, 1320], 60);
      return;
    }
    if (c.tipo === 'burbuja') {
      escudo = true; pintarVidas();
      flotar(c.x, c.y - 10, '¡Escudo! 🛡️', '#3d72c4');
      arpegio([520, 780], 80);
      return;
    }
    racha++; mejorRacha = Math.max(mejorRacha, racha); atrapados++;
    const m = multiplicador();
    const base = c.tipo === 'oro' ? 5 : c.tipo === 'carta' ? 3 : 1;
    puntos += base * m;
    ale.atrapa = ahora + 260;
    if (c.tipo === 'carta') {
      flotar(W / 2, BOCA - 90, FRASES_CARTA[Math.floor(Math.random() * FRASES_CARTA.length)], '#8d1f2e', 22, 2400);
      arpegio([784, 988, 1175], 70);
    } else tono(c.tipo === 'oro' ? 1175 : 740 + Math.min(racha, 30) * 12, .07);
    flotar(c.x, c.y - 8, `+${base * m}`, c.tipo === 'oro' ? '#a8781f' : '#e0303f', c.tipo === 'oro' ? 22 : 18);
    chispazo(c.x, c.y, c.tipo === 'oro' ? ['#f7c948', '#fff6c8'] : ['#e0303f', '#ff8a8f', '#ffd3d6']);
    if (racha === 10 || racha === 25) {
      banner = { txt: `¡Racha x${m}! 🔥`, hasta: ahora + 1200 };
      arpegio([880, 1100, 1320, 1760], 55);
    }
    const nuevoNivel = 1 + Math.floor(puntos / 30);
    if (nuevoNivel > nivel) {
      nivel = nuevoNivel; baile = ahora + 1300;
      banner = { txt: `¡Nivel ${nivel}! ✨`, hasta: ahora + 1400 };
      arpegio([523, 659, 784, 1047], 80);
    }
    pintarPuntos();
  }

  function paso(ahora) {
    if (estado !== 'jugando' && estado !== 'cuenta') return;
    const dt = Math.min(50, ahora - (ultimo || ahora)); ultimo = ahora;
    ale.x += (ale.destino - ale.x) * Math.min(1, dt / 90);
    if (estado === 'cuenta') {
      if (ahora >= cuentaHasta) { estado = 'jugando'; proxima = ahora + 300; tono(1047, .12); }
    } else {
      if (ahora >= proxima) soltar(ahora);
      cosas = cosas.filter(c => {
        c.y += c.v * dt / 16;
        // con el imán, los corazones, cartas y dorados vuelan hacia Alejandro
        if (iman > ahora && c.tipo !== 'nube' && c.y > 40) c.x += (ale.x - c.x) * Math.min(1, dt / 220);
        if (c.y > BOCA - 10 && c.y < BOCA + 26 && Math.abs(c.x - ale.x) < 34) { atrapar(c, ahora); return false; }
        if (c.y > H + 20) {
          if (c.tipo === 'corazon' || c.tipo === 'oro') racha = 0, pintarPuntos();   // se escapó: solo se corta la racha
          return false;
        }
        return true;
      });
    }
    chispas = chispas.filter(p => { p.x += p.vx * dt / 16; p.y += p.vy * dt / 16; p.vy += .15 * dt / 16; p.vida -= dt / 600; return p.vida > 0; });
    textos = textos.filter(t => { t.y -= .5 * dt / 16; t.vida -= dt / t.dur; return t.vida > 0; });
    dibujar(ahora);
    if (estado === 'jugando' || estado === 'cuenta') requestAnimationFrame(paso);
  }

  function prepararFondo() {
    nubesFondo = [0, 1, 2].map(i => ({ x: Math.random() * W, y: 30 + i * 46, v: .12 + i * .06, t: 3 + i * .6 }));
  }

  function empezar() {
    if (estado === 'pausa') { reanudar(); return; }
    hoja = new Image();
    hoja.src = urlDisfraz(disfrazActual);
    puntos = 0; vidas = 3; cosas = []; chispas = []; textos = []; ultimo = 0; proxima = 0;
    racha = 0; mejorRacha = 0; nivel = 1; atrapados = 0;
    iman = 0; escudo = false; invulnerable = 0; mareo = 0; baile = 0; sacudida = 0; banner = null;
    ale = { x: W / 2, destino: W / 2, atrapa: 0 };
    prepararFondo(); pintarPuntos(); pintarVidas();
    $('juegoPantalla').hidden = true;
    estado = 'cuenta'; cuentaHasta = performance.now() + 2100;
    arpegio([523, 523, 523], 700);
    requestAnimationFrame(paso);
  }

  function pausar() {
    if (estado !== 'jugando' && estado !== 'cuenta') return;
    estado = 'pausa';
    $('juegoMensaje').textContent = 'Pausa ⏸️ Alejandro te espera.';
    $('juegoEmpezar').textContent = 'Seguir jugando';
    $('juegoPantalla').hidden = false;
  }
  function reanudar() {
    $('juegoPantalla').hidden = true;
    estado = 'cuenta'; ultimo = 0;
    const ahora = performance.now(), corrimiento = 2100;
    cuentaHasta = ahora + corrimiento;
    if (iman > 0) iman += corrimiento;
    requestAnimationFrame(paso);
  }

  function terminar() {
    estado = 'fin';
    const record = leerRecord();
    const nuevo = puntos > record;
    if (nuevo) { guardarJSON('dallanaRecordJuego', puntos); pintarRecord(); }
    const medalla = MEDALLAS.find(([min]) => puntos >= min);
    let msg = `${medalla ? medalla[1] + ' ' : ''}¡Atrapaste ${puntos} ${puntos === 1 ? 'punto' : 'puntos'}!`;
    if (nuevo && record) msg += ' 🎉 ¡Nuevo récord!';
    msg += `\nMejor racha: ${mejorRacha} · Nivel ${nivel}`;
    if (puntos >= 20 && leerJSON('dallanaJuegoCorazon', '') !== hoyLocal()) {
      guardarJSON('dallanaJuegoCorazon', hoyLocal());
      sumarCorazon();
      msg += '\nGanaste un corazón del día 💗';
    } else if (!medalla) msg += '\nCon 10 puntos ganas tu primera medalla 🥉';
    $('juegoMensaje').textContent = msg;
    $('juegoEmpezar').textContent = 'Jugar otra vez';
    $('juegoPantalla').hidden = false;
    arpegio(nuevo ? [523, 659, 784, 1047, 1319] : [659, 523, 392], 110);
    if (nuevo) {
      notificar(`hizo un nuevo récord en el juego de Alejandro: ${puntos} puntos${medalla ? ' ' + medalla[1] : ''} 🎮`, 'video_game');
      lanzarCelebracion();
    }
  }

  function abrirJuego() {
    cerrarAlejandro(false);
    estado = 'menu';
    $('juegoMensaje').textContent = 'Mueve a Alejandro con el dedo (o con las flechas) y atrapa los corazones. ¡Ojo con las nubecitas de lluvia!';
    $('juegoEmpezar').textContent = '¡Jugar!';
    $('juegoPantalla').hidden = false;
    pintarRecord(); vidas = 3; escudo = false; puntos = 0; racha = 0; pintarVidas(); pintarPuntos(); pintarSonido();
    prepararFondo();
    hoja = new Image(); hoja.onload = () => dibujar(performance.now()); hoja.src = urlDisfraz(disfrazActual);
    dibujar(performance.now());
    if (!dlg.open) dlg.showModal();
    notificar('abrió el juego de atrapar corazones 🎮', 'video_game');
  }

  // mover con el dedo o el mouse (en el lienzo) y con las flechas
  const mover = e => {
    const r = cv.getBoundingClientRect();
    ale.destino = Math.max(24, Math.min(W - 24, (e.clientX - r.left) * W / r.width));
  };
  cv.addEventListener('pointerdown', e => { mover(e); cv.setPointerCapture?.(e.pointerId); });
  cv.addEventListener('pointermove', e => { if (e.pointerType === 'mouse' || e.buttons || e.pressure) mover(e); });
  dlg.addEventListener('keydown', e => {
    if (estado !== 'jugando' && estado !== 'cuenta') return;
    if (e.key === 'ArrowLeft') { ale.destino = Math.max(24, ale.destino - 40); e.preventDefault(); }
    if (e.key === 'ArrowRight') { ale.destino = Math.min(W - 24, ale.destino + 40); e.preventDefault(); }
    if (e.key === 'p' || e.key === 'P') pausar();
  });
  dlg.addEventListener('close', () => { estado = 'menu'; });
  document.addEventListener('visibilitychange', () => { if (document.visibilityState !== 'visible') pausar(); });
  $('juegoEmpezar').addEventListener('click', empezar);
  $('juegoSonido')?.addEventListener('click', () => {
    sonido = !sonido; guardarJSON('dallanaJuegoSonido', sonido); pintarSonido();
    if (sonido) tono(880, .08);
  });
  $('juegoAbrir')?.addEventListener('click', abrirJuego);
  $('menuJuego')?.addEventListener('click', abrirJuego);
  pintarRecord();
})();

/* ============================================================
   STICKERS QUE REACCIONAN: al tocarlos saltan (o giran, bailan, laten), sueltan corazoncitos
   y dicen algo distinto cada vez. Los que va descubriendo quedan en dallanaStickers;
   al descubrirlos todos, Alejandro la felicita.
   ============================================================ */
const FRASES_STICKERS = {
  'stikers': ['¡Flores para ti! 🌹', 'Una rosa para la más linda 🌹'],
  'stikers1': ['Te quiero un montón 💕', 'Más que ayer, menos que mañana 💕'],
  'stikers2': ['¡Abrazo de Snoopy! 🤗', 'Abrazo apretadito 🤗'],
  'stikers3': ['¡Erupción de amor! 🌋', 'Así de fuerte te quiero 🌋'],
  'stikers4': ['¿Vamos de excursión? 🎒', 'Contigo voy a donde sea 🎒'],
  'stikers5': ['Te llegó correo 💌', 'Revisa tu buzón, quizás hay algo 💌'],
  'stikers6': ['¡Guau guau! 🐾', 'Huellitas para ti 🐾'],
  'stikers7': ['¡Guau! Más mimos, por favor 🐶', 'Rásquenme la guatita 🐶'],
  'stikers8': ['¡Guau! 💗', '¿Jugamos? 🎾'],
  'stikers9': ['Tranquila, tú eres la más fuerte ✨', 'Respira, todo va a salir bien ✨'],
  'stikers10': ['¡Hola desde aquí arriba! 👋', '¡Te estaba esperando! 👋'],
  'stikers11': ['Con esta venda igual veo que eres la más linda 😎', 'Ni con los ojos tapados me pierdo de ti 😎'],
  'stikers12': ['¡Eres increíble! 💪', '¡Tú puedes con todo! 💪'],
  'stikers13': ['Hora de descansar, ya trabajaste mucho ☕', 'Un cafecito y seguimos ☕'],
  'stikers14': ['Estas flores son para ti 💐', 'Un ramo para alegrarte el día 💐'],
  'stikers15': ['¡Mira mi gatito! 🐱', 'Miau 🐱'],
  'stikers16': ['Jajaja, eres lo máximo 🪭', 'Tu risa es mi favorita 🪭'],
  'stikers17': ['¡Rawr! (de cariño) 🔥', 'Rawr significa te quiero en dinosaurio 🔥'],
  'stikers18': ['¡Soy un dinosaurio de verdad! 🦖', '¡Rawr! Alejandro es mi primo 🦖'],
  'stikers19': ['Globos para la mejor 🎈', '¡Que no se vuelen! 🎈'],
  'stikers20': ['Así de enamorados 💞', 'Tú y yo 💞'],
  'stikers21': ['Un corazón para ti 💚', 'Corazón verde, de esperanza 💚'],
  'stikers22': ['Floreciendo contigo 🌸', 'Contigo todo florece 🌸'],
  // perritos pastor alemán (los 12 se turnan: cada visita aparecen 6 distintos)
  'perrito1': ['Esperándote echadito 🐾', 'Modo siesta activado 💤'],
  'perrito2': ['¿Me das un premio? 🦴', 'Soy un buen chico 🐶'],
  'perrito3': ['Te traje mi juguete favorito 🐰', '¡Lo cuidé para ti! 🐰'],
  'perrito4': ['¿Me veo linda con mi rosita? 🎀', 'Me puse elegante para ti 🎀'],
  'perrito5': ['¡Asomándome! 👀', '¿Hay alguien ahí? 👀'],
  'perrito6': ['Te extraño cuando no estás 🥺', 'Un abrazo y se me pasa 🥺'],
  'perrito7': ['¡Llegaste! ¡Llegaste! 🐕', '¡Qué felicidad verte! 💛'],
  'perrito8': ['Grrr… (es de mentira) 😤', 'Hoy ando gruñón, pero te quiero 😤'],
  'perrito9': ['¡Hola, mamá! 👋✨', '¡Choca esa patita! 🐾'],
  'perrito10': ['¡Voy corriendo a verte! 💨', '¡Espérame! 💨'],
  'perrito11': ['Glu glu glu… ¡toma agüita tú también! 💧', 'Hidratándome para jugar contigo 💧'],
  'perrito12': ['¿Jugamos a la pelota? 🎾', '¡Tírala otra vez! 🎾']
};
const PERRITOS = Array.from({ length: 12 }, (_, i) => `perrito${i + 1}`);
// cada visita pone 6 perritos distintos en las esquinas de abajo (antes de que carguen: son lazy)
(() => {
  const lugares = [...document.querySelectorAll('img.perrito')];
  const mezcla = [...PERRITOS].sort(() => Math.random() - .5);
  lugares.forEach((img, i) => { img.src = `assets/stickers/${mezcla[i % mezcla.length]}.png`; });
})();
(() => {
  const selector = '.sticker, .letter-sticker, .postal-sticker, .nota-sticker';
  const ANIMACIONES = ['sticker-salta', 'sticker-gira', 'sticker-baila', 'sticker-late'];
  const SIMBOLOS = ['♥', '♡', '✿', '✧'];
  const COLORES = ['#e0303f', '#ff8a8f', '#f2c14e', '#6fa0e8', '#4f9a4a'];
  const vistos = leerSet('dallanaStickers');
  const toques = {};
  const nombreDe = st => (st.getAttribute('src') || '').split('/').pop().replace(/\.(png|jpe?g|gif|webp)(\?.*)?$/, '');
  // cuentan los que están en la página más los 12 perritos (aunque hoy solo se vean 6)
  const totalStickers = () => new Set([...document.querySelectorAll(selector)].map(nombreDe).filter(n => FRASES_STICKERS[n]).concat(PERRITOS)).size;
  const suave = matchMedia('(prefers-reduced-motion: reduce)');

  function corazoncitos(r) {
    if (suave.matches) return;
    for (let i = 0; i < 7; i++) {
      const c = document.createElement('span');
      c.className = 'sticker-corazon';
      c.textContent = SIMBOLOS[i % SIMBOLOS.length];
      c.style.left = `${r.left + scrollX + r.width / 2}px`;
      c.style.top = `${r.top + scrollY + r.height / 3}px`;
      c.style.color = COLORES[i % COLORES.length];
      c.style.setProperty('--dx', `${Math.round((Math.random() - .5) * 120)}px`);
      c.style.setProperty('--dy', `${Math.round(-50 - Math.random() * 70)}px`);
      c.style.setProperty('--rot', `${Math.round((Math.random() - .5) * 120)}deg`);
      c.style.animationDelay = `${i * 30}ms`;
      document.body.append(c);
      setTimeout(() => c.remove(), 1200);
    }
  }

  function globo(st, texto, extra) {
    document.querySelectorAll('.sticker-globo').forEach(g => g.remove());
    const g = document.createElement('span');
    g.className = 'sticker-globo';
    g.textContent = texto;
    if (extra) { const s = document.createElement('small'); s.textContent = extra; g.append(s); }
    document.body.append(g);
    const r = st.getBoundingClientRect();
    const x = Math.max(8, Math.min(innerWidth - 8 - g.offsetWidth, r.left + r.width / 2 - g.offsetWidth / 2));
    const arriba = r.top - g.offsetHeight - 8 > 4;
    g.style.left = `${x + scrollX}px`;
    g.style.top = `${(arriba ? r.top - g.offsetHeight - 8 : r.bottom + 8) + scrollY}px`;
    g.style.setProperty('--cola', `${Math.round(r.left + r.width / 2 - x)}px`);
    g.classList.toggle('abajo', !arriba);
    setTimeout(() => g.classList.add('fuera'), 2400);
    setTimeout(() => g.remove(), 2900);
  }

  document.addEventListener('click', e => {
    const st = e.target.closest?.(selector); if (!st) return;
    const nombre = nombreDe(st);
    const frases = FRASES_STICKERS[nombre] || ['💗'];
    toques[nombre] = (toques[nombre] || 0) + 1;
    // animación distinta cada vez
    ANIMACIONES.forEach(a => st.classList.remove(a)); void st.offsetWidth;
    const anim = ANIMACIONES[(toques[nombre] - 1) % ANIMACIONES.length];
    st.classList.add(anim);
    setTimeout(() => st.classList.remove(anim), 800);
    corazoncitos(st.getBoundingClientRect());
    try { navigator.vibrate?.(12); } catch {}
    // colección
    let extra = '';
    if (FRASES_STICKERS[nombre] && !vistos.has(nombre)) {
      vistos.add(nombre); guardarSet('dallanaStickers', vistos);
      const total = totalStickers(), n = [...vistos].filter(v => FRASES_STICKERS[v]).length;
      extra = `✨ Sticker descubierto ${Math.min(n, total)} de ${total}`;
      if (n >= total && total > 0 && !leerJSON('dallanaStickersCompletos', false)) {
        guardarJSON('dallanaStickersCompletos', true);
        setTimeout(() => {
          lanzarCelebracion();
          alejandroReacciona('aplaudir', 2400);
          alejandroDice(`¡Encontraste los ${total} stickers, mamá! Eres la mejor exploradora del rincón. 🏆💗`, 'Alejandro 🦀', null, true);
          notificar(`descubrió los ${total} stickers de la página 🏆`, 'trophy');
        }, 900);
      }
    }
    globo(st, frases[(toques[nombre] - 1) % frases.length], extra);
  });
})();

/* ============================================================
   SERVIDOR DEL RINCÓN (Cloudflare): clave de Dallana y respaldo de su progreso
   Solo se usa si URL_RINCON tiene la dirección del servidor (rincon-servidor/GUIA.md).
   ============================================================ */
var tokenRincon = (() => { try { return localStorage.getItem('dallanaToken') || ''; } catch { return ''; } })();
var respaldoPendiente = false;   // var: guardarJSON la usa desde el comienzo de la página
function marcarRespaldo() { respaldoPendiente = true; }

async function rincon(ruta, opciones = {}) {
  if (!tokenRincon) throw new Error('sin clave');
  const r = await fetch(`${URL_RINCON}${ruta}`, {
    ...opciones,
    headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${tokenRincon}`, ...(opciones.headers || {}) }
  });
  if (r.status === 401) {
    tokenRincon = '';
    try { localStorage.removeItem('dallanaToken'); } catch {}
    pedirClave();
    throw new Error('sin clave');
  }
  if (!r.ok) throw new Error(String(r.status));
  return r.json();
}

function pedirClave() {
  const dlg = $('claveDialog');
  if (!URL_RINCON || !dlg || dlg.open) return;
  if (document.querySelector('dialog[open]') || $('welcome')?.matches(':not(.closed)')) { setTimeout(pedirClave, 3000); return; }
  $('claveEstado').textContent = '';
  dlg.showModal();
  setTimeout(() => $('claveInput')?.focus(), 60);
}

$('claveForm')?.addEventListener('submit', async e => {
  e.preventDefault();
  const pin = ($('claveInput')?.value || '').trim(); if (!pin) return;
  const estado = $('claveEstado'), btn = $('claveEntrar');
  btn.disabled = true; estado.textContent = 'Alejandro está revisando la clave… 🦀';
  try {
    const r = await fetch(`${URL_RINCON}/api/entrar`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ pin }) });
    const d = await r.json().catch(() => ({}));
    if (!r.ok || !d.token) { estado.textContent = d.error || 'Esa no es nuestra clave. Prueba otra vez 💗'; return; }
    tokenRincon = d.token;
    try { localStorage.setItem('dallanaToken', d.token); } catch {}
    $('claveInput').value = '';
    $('claveDialog').close();
    alejandroReacciona('aplaudir', 1600);
    alejandroDice('¡Listo, mamá! Ahora tu buzón y tus cosas están guardados y protegidos. 🔐💗', 'Alejandro 🦀', null, true);
    await restaurarProgreso();
    revisarCartas();
  } catch {
    estado.textContent = 'No pude conectarme. Revisa tu internet y prueba otra vez.';
  } finally {
    btn.disabled = false;
  }
});

/* Respaldo: todo lo que la página guarda (dallana…) se sube al servidor cada minuto si cambió */
const SIN_RESPALDO = ['dallanaToken', 'dallanaYo'];
function progresoLocal() {
  const datos = {};
  try {
    for (let i = 0; i < localStorage.length; i++) {
      const k = localStorage.key(i);
      if (k && k.startsWith('dallana') && !SIN_RESPALDO.includes(k)) datos[k] = localStorage.getItem(k);
    }
  } catch {}
  return datos;
}
function subirRespaldo(keepalive = false) {
  if (!URL_RINCON || !tokenRincon || !respaldoPendiente) return;
  respaldoPendiente = false;
  rincon('/api/progreso', { method: 'PUT', keepalive, body: JSON.stringify({ guardado: Date.now(), datos: progresoLocal() }) })
    .catch(() => { respaldoPendiente = true; });
}
// En un teléfono nuevo (o con los datos borrados) recupera lo que falte
async function restaurarProgreso() {
  try {
    const { datos = {} } = await rincon('/api/progreso');
    let recuperados = 0;
    for (const [k, v] of Object.entries(datos)) {
      if (SIN_RESPALDO.includes(k)) continue;
      try { if (localStorage.getItem(k) === null) { localStorage.setItem(k, v); recuperados++; } } catch {}
    }
    if (recuperados) location.reload();
    else marcarRespaldo();
  } catch {}
}
if (URL_RINCON) {
  setInterval(() => subirRespaldo(), 60000);
  document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'hidden') subirRespaldo(true); });
}

/* ============================================================
   PANTALLA DE CARGA: los corazones se llenan según lo que va cargando
   ============================================================ */
(() => {
  const carga = $('carga'); if (!carga) return;
  const corazones = [...document.querySelectorAll('#cargaBarra i')];
  const inicio = performance.now();
  let progreso = 0, terminado = false;
  const pintar = frac => {
    progreso = Math.max(progreso, frac);
    const n = Math.round(progreso * corazones.length);
    corazones.forEach((c, k) => c.classList.toggle('llena', k < n));
  };
  const imagenes = [...document.images];
  const contar = () => {
    if (terminado) return;
    const listas = imagenes.filter(im => im.complete).length;
    pintar(.15 + .75 * (imagenes.length ? listas / imagenes.length : 1));
  };
  imagenes.forEach(im => { if (!im.complete) { im.addEventListener('load', contar, { once: true }); im.addEventListener('error', contar, { once: true }); } });
  contar();
  const terminar = () => {
    if (terminado) return;
    terminado = true;
    pintar(1);
    // se queda al menos un ratito para que se vea a Alejandro corriendo
    const espera = Math.max(0, 1100 - (performance.now() - inicio));
    setTimeout(() => { carga.classList.add('lista'); setTimeout(() => carga.remove(), 600); }, espera + 250);
  };
  const listo = () => (document.fonts ? document.fonts.ready.catch(() => {}) : Promise.resolve()).then(terminar);
  if (document.readyState === 'complete') listo();
  else addEventListener('load', listo, { once: true });
  setTimeout(terminar, 6000);   // por si alguna imagen nunca termina (sin internet)
})();

/* ============================================================
   CAMBIO DE DÍA SIN RECARGAR: a medianoche se vacían los corazones y cuenta el día nuevo
   ============================================================ */
let diaActual = hoyLocal();
setInterval(() => {
  const hoy = hoyLocal();
  if (hoy === diaActual) return;
  diaActual = hoy;
  actualizarProgreso();
  registrarDia();
  actualizarContador();
}, 30000);

/* ============================================================
   INICIALIZACIÓN
   ============================================================ */
avisarVisita();
actualizarContador();
registrarDia();
actualizarProgreso();
if (!$('welcome')) saludoAlejandro();
estadoAlejandro();
pintarSobre();
programarPaseo();
actualizarBotonFavoritos();
renderContenido();
cargarContenido();
setInterval(actualizarContador, 30000);
pintarPostal();
setInterval(pintarPostal, 600000);
if (!$('welcome')) setTimeout(escribirNombre, 400);

if ('serviceWorker' in navigator && (location.protocol === 'https:' || location.hostname === 'localhost' || location.hostname === '127.0.0.1')) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('./sw.js').catch(() => {});
  });
}

