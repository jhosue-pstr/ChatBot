(function() {
  "use strict";

  // Función para manejar la selección de idioma
  function handleLanguageSelection(language) {
    // Ocultar todos los checkmarks
    document.querySelectorAll('.bi-check').forEach((check) => check.style.visibility = 'hidden');

    // Mostrar el checkmark del idioma seleccionado
    if (language === 'Español') {
      document.getElementById('checkSpanish').style.visibility = 'visible';
    } else if (language === 'English') {
      document.getElementById('checkEnglish').style.visibility = 'visible';
    }
    // Actualizar el texto del botón
    document.getElementById('dropdownLangCurrency').innerHTML = `${language} / ${document.getElementById('dropdownLangCurrency').innerHTML.split(' / ')[1]}`;
  }

  // Función para manejar la selección de moneda
  function handleCurrencySelection(currency) {
    // Ocultar todos los checkmarks de moneda
    document.querySelectorAll('.bi-check').forEach((check) => check.style.visibility = 'hidden');

    // Mostrar el checkmark de la moneda seleccionada
    if (currency === 'PEN') {
      document.getElementById('checkPEN').style.visibility = 'visible';
    } else if (currency === 'USD') {
      document.getElementById('checkPEN').style.visibility = 'hidden';
    }
    // Actualizar el texto del botón
    document.getElementById('dropdownLangCurrency').innerHTML = `${document.getElementById('dropdownLangCurrency').innerHTML.split(' / ')[0]} / ${currency}`;
  }

  // Agregar eventos para el idioma
  document.getElementById('selectEnglish').addEventListener('click', function() {
    handleLanguageSelection('English');
  });
  document.getElementById('selectSpanish').addEventListener('click', function() {
    handleLanguageSelection('Español');
  });

  // Agregar eventos para la moneda
  document.getElementById('selectPEN').addEventListener('click', function() {
    handleCurrencySelection('PEN');
  });
  document.getElementById('selectUSD').addEventListener('click', function() {
    handleCurrencySelection('USD');
  });




  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }
  mobileNavToggleBtn.addEventListener('click', mobileNavToogle);

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });
  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.navmenu .toggle-dropdown').forEach(navmenu => {
    navmenu.addEventListener('click', function(e) {
      e.preventDefault();
      this.parentNode.classList.toggle('active');
      this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
      e.stopImmediatePropagation();
    });
  });

  /**
   * Preloader
   */
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove();
    });
  }

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  scrollTop.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  /**
   * Auto generate the carousel indicators
   */
  document.querySelectorAll('.carousel-indicators').forEach((carouselIndicator) => {
    carouselIndicator.closest('.carousel').querySelectorAll('.carousel-item').forEach((carouselItem, index) => {
      if (index === 0) {
        carouselIndicator.innerHTML += `<li data-bs-target="#${carouselIndicator.closest('.carousel').id}" data-bs-slide-to="${index}" class="active"></li>`;
      } else {
        carouselIndicator.innerHTML += `<li data-bs-target="#${carouselIndicator.closest('.carousel').id}" data-bs-slide-to="${index}"></li>`;
      }
    });
  });

  /**
   * Initiate glightbox
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  /**
   * Initiate Pure Counter
   */
  new PureCounter();

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function(swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }

  window.addEventListener("load", initSwiper);

  /**
   * Frequently Asked Questions Toggle
   */
  document.querySelectorAll('.faq-item h3, .faq-item .faq-toggle').forEach((faqItem) => {
    faqItem.addEventListener('click', () => {
      faqItem.parentNode.classList.toggle('faq-active');
    });
  });

  /**
   * Correct scrolling position upon page load for URLs containing hash links.
   */
  window.addEventListener('load', function(e) {
    if (window.location.hash) {
      if (document.querySelector(window.location.hash)) {
        setTimeout(() => {
          let section = document.querySelector(window.location.hash);
          let scrollMarginTop = getComputedStyle(section).scrollMarginTop;
          window.scrollTo({
            top: section.offsetTop - parseInt(scrollMarginTop),
            behavior: 'smooth'
          });
        }, 100);
      }
    }
  });

  /**
   * Navmenu Scrollspy
   */
  let navmenulinks = document.querySelectorAll('.navmenu a');

  function navmenuScrollspy() {
    navmenulinks.forEach(navmenulink => {
      if (!navmenulink.hash) return;
      let section = document.querySelector(navmenulink.hash);
      if (!section) return;
      let position = window.scrollY + 200;
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        document.querySelectorAll('.navmenu a.active').forEach(link => link.classList.remove('active'));
        navmenulink.classList.add('active');
      } else {
        navmenulink.classList.remove('active');
      }
    })
  }
  window.addEventListener('load', navmenuScrollspy);
  document.addEventListener('scroll', navmenuScrollspy);

  ///////////////////////////////////


































  // Constantes del chatbot
  const input = document.getElementById('chat-input');
  const sendBtn = document.getElementById('chat-send');
  const messages = document.getElementById('chat-messages');

  // Función para agregar mensajes al chat con avatar
  function addMessage(text, sender) {
    const div = document.createElement('div');
    div.classList.add('message', sender);

    const avatar = document.createElement('img');
    avatar.classList.add('avatar');

    // Usar las rutas relativas para las imágenes de acuerdo con la ubicación de los archivos
    avatar.src = sender === 'user' ? 'assets/img/usuario.png' : 'assets/img/botxd.jpg';
    avatar.alt = sender === 'user' ? 'Usuario' : 'Chatbot';


    const messageText = document.createElement('div');
    messageText.classList.add('text');
    messageText.innerHTML = text;  // Interpretar HTML

    div.appendChild(avatar);
    div.appendChild(messageText);

    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }

  // Array de saludos y palabras para mostrar menú
  const palabrasMenu = [
    'hola', 'buenos días', 'buenas tardes', 'buenas noches', 'hey', 'buen día', 'qué tal', 'buenas',
    'menu', 'menu de opciones', 'opciones', 'tabla'
  ];

  function contienePalabraMenu(texto) {
    return palabrasMenu.some(palabra => texto.includes(palabra));
  }

  async function getResponse(message) {
    const lower = message.toLowerCase();

    // Mostrar menú si alguna palabra de menú está en el mensaje
    if (contienePalabraMenu(lower)) {
      return `¡Hola! Soy tu asistente virtual para la hackatón de Ingeniería de Sistemas.<br>
      ¿En qué puedo ayudarte hoy? Selecciona una opción o escribe tu pregunta.<br>
      1. Información sobre la hackatón.<br>
      2. Asistencia técnica.<br>
      3. Recordatorios importantes.<br>
      4. Recursos útiles.<br>
      5. Preguntas generales.`;
    }

    if (lower === '1' || lower.includes('información sobre la hackatón')) {
      return `La hackatón comienza el 1 de junio y termina el 3 de junio. Los premios son...<br>
      ¿Te gustaría conocer la agenda del evento?`;
    }

    if (lower === '2' || lower.includes('asistencia técnica')) {
      return '¿En qué lenguaje o tecnología necesitas ayuda? (Ej. Python, JavaScript, APIs)';
    }

    if (lower === '3' || lower.includes('recordatorios')) {
      return 'Recuerda que el plazo de inscripción cierra el 30 de mayo. También, el primer taller será el 1 de junio a las 9:00 AM.';
    }

    if (lower === '4' || lower.includes('recursos')) {
      return 'Aquí tienes un enlace a tutoriales sobre Python: https://www.python.org/about/gettingstarted/';
    }

    if (lower === '5' || lower.includes('preguntas generales')) {
      return 'Puedes preguntarme cosas como: ¿Cómo me registro en la hackatón? o ¿Qué lenguajes puedo usar?';
    }

    if (lower.includes('github')) {
      return 'Para subir tu código a GitHub, primero crea un repositorio, luego usa git add, commit y push. Aquí tienes un tutorial: https://docs.github.com/es/github/using-git';
    }

    // Si no coincide, llama a IA
    try {
      const res = await fetch("https://openrouter.ai/api/v1/chat/completions", {
        method: "POST",
        headers: {
          "Authorization": "Bearer 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",
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
          "messages": [
            {
              "role": "user",
              "content": message
            }
          ]
        })
      });


      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }

      const data = await res.json();
      return data.choices[0].message.content; // Ajusta según la estructura real de la respuesta
    } catch (error) {
      console.error(error);
      return "Lo siento, no puedo responder ahora. Por favor intenta más tarde.";
    }
  }

  // Manejar evento de enviar mensaje
  sendBtn.addEventListener('click', async () => {
    const text = input.value.trim();
    if (!text) return;
    addMessage(text, 'user');
    input.value = '';

    const response = await getResponse(text);
    addMessage(response, 'bot');
  });

  // Permitir enviar con tecla Enter
  input.addEventListener('keydown', e => {
    if (e.key === 'Enter') sendBtn.click();
  });
  

})();
