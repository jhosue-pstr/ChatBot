(function () {
  "use strict";

  // Función para manejar la selección de idioma
  function handleLanguageSelection(language) {
    // Ocultar todos los checkmarks
    document
      .querySelectorAll(".bi-check")
      .forEach((check) => (check.style.visibility = "hidden"));

    // Mostrar el checkmark del idioma seleccionado
    if (language === "Español") {
      document.getElementById("checkSpanish").style.visibility = "visible";
    } else if (language === "English") {
      document.getElementById("checkEnglish").style.visibility = "visible";
    }
    // Actualizar el texto del botón
    document.getElementById(
      "dropdownLangCurrency"
    ).innerHTML = `${language} / ${
      document.getElementById("dropdownLangCurrency").innerHTML.split(" / ")[1]
    }`;
  }

  // Función para manejar la selección de moneda
  function handleCurrencySelection(currency) {
    // Ocultar todos los checkmarks de moneda
    document
      .querySelectorAll(".bi-check")
      .forEach((check) => (check.style.visibility = "hidden"));

    // Mostrar el checkmark de la moneda seleccionada
    if (currency === "PEN") {
      document.getElementById("checkPEN").style.visibility = "visible";
    } else if (currency === "USD") {
      document.getElementById("checkPEN").style.visibility = "hidden";
    }
    // Actualizar el texto del botón
    document.getElementById("dropdownLangCurrency").innerHTML = `${
      document.getElementById("dropdownLangCurrency").innerHTML.split(" / ")[0]
    } / ${currency}`;
  }

  // Agregar eventos para el idioma
  document
    .getElementById("selectEnglish")
    .addEventListener("click", function () {
      handleLanguageSelection("English");
    });
  document
    .getElementById("selectSpanish")
    .addEventListener("click", function () {
      handleLanguageSelection("Español");
    });

  // Agregar eventos para la moneda
  document.getElementById("selectPEN").addEventListener("click", function () {
    handleCurrencySelection("PEN");
  });
  document.getElementById("selectUSD").addEventListener("click", function () {
    handleCurrencySelection("USD");
  });

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector("body");
    const selectHeader = document.querySelector("#header");
    if (
      !selectHeader.classList.contains("scroll-up-sticky") &&
      !selectHeader.classList.contains("sticky-top") &&
      !selectHeader.classList.contains("fixed-top")
    )
      return;
    window.scrollY > 100
      ? selectBody.classList.add("scrolled")
      : selectBody.classList.remove("scrolled");
  }

  document.addEventListener("scroll", toggleScrolled);
  window.addEventListener("load", toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector(".mobile-nav-toggle");

  function mobileNavToogle() {
    document.querySelector("body").classList.toggle("mobile-nav-active");
    mobileNavToggleBtn.classList.toggle("bi-list");
    mobileNavToggleBtn.classList.toggle("bi-x");
  }
  mobileNavToggleBtn.addEventListener("click", mobileNavToogle);

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll("#navmenu a").forEach((navmenu) => {
    navmenu.addEventListener("click", () => {
      if (document.querySelector(".mobile-nav-active")) {
        mobileNavToogle();
      }
    });
  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll(".navmenu .toggle-dropdown").forEach((navmenu) => {
    navmenu.addEventListener("click", function (e) {
      e.preventDefault();
      this.parentNode.classList.toggle("active");
      this.parentNode.nextElementSibling.classList.toggle("dropdown-active");
      e.stopImmediatePropagation();
    });
  });

  /**
   * Preloader
   */
  const preloader = document.querySelector("#preloader");
  if (preloader) {
    window.addEventListener("load", () => {
      preloader.remove();
    });
  }

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector(".scroll-top");

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100
        ? scrollTop.classList.add("active")
        : scrollTop.classList.remove("active");
    }
  }
  scrollTop.addEventListener("click", (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });

  window.addEventListener("load", toggleScrollTop);
  document.addEventListener("scroll", toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: "ease-in-out",
      once: true,
      mirror: false,
    });
  }
  window.addEventListener("load", aosInit);

  /**
   * Auto generate the carousel indicators
   */
  document
    .querySelectorAll(".carousel-indicators")
    .forEach((carouselIndicator) => {
      carouselIndicator
        .closest(".carousel")
        .querySelectorAll(".carousel-item")
        .forEach((carouselItem, index) => {
          if (index === 0) {
            carouselIndicator.innerHTML += `<li data-bs-target="#${
              carouselIndicator.closest(".carousel").id
            }" data-bs-slide-to="${index}" class="active"></li>`;
          } else {
            carouselIndicator.innerHTML += `<li data-bs-target="#${
              carouselIndicator.closest(".carousel").id
            }" data-bs-slide-to="${index}"></li>`;
          }
        });
    });

  /**
   * Initiate glightbox
   */
  const glightbox = GLightbox({
    selector: ".glightbox",
  });

  /**
   * Initiate Pure Counter
   */
  new PureCounter();

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function (swiperElement) {
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
  document
    .querySelectorAll(".faq-item h3, .faq-item .faq-toggle")
    .forEach((faqItem) => {
      faqItem.addEventListener("click", () => {
        faqItem.parentNode.classList.toggle("faq-active");
      });
    });

  /**
   * Correct scrolling position upon page load for URLs containing hash links.
   */
  window.addEventListener("load", function (e) {
    if (window.location.hash) {
      if (document.querySelector(window.location.hash)) {
        setTimeout(() => {
          let section = document.querySelector(window.location.hash);
          let scrollMarginTop = getComputedStyle(section).scrollMarginTop;
          window.scrollTo({
            top: section.offsetTop - parseInt(scrollMarginTop),
            behavior: "smooth",
          });
        }, 100);
      }
    }
  });

  /**
   * Navmenu Scrollspy
   */
  let navmenulinks = document.querySelectorAll(".navmenu a");

  function navmenuScrollspy() {
    navmenulinks.forEach((navmenulink) => {
      if (!navmenulink.hash) return;
      let section = document.querySelector(navmenulink.hash);
      if (!section) return;
      let position = window.scrollY + 200;
      if (
        position >= section.offsetTop &&
        position <= section.offsetTop + section.offsetHeight
      ) {
        document
          .querySelectorAll(".navmenu a.active")
          .forEach((link) => link.classList.remove("active"));
        navmenulink.classList.add("active");
      } else {
        navmenulink.classList.remove("active");
      }
    });
  }
  window.addEventListener("load", navmenuScrollspy);
  document.addEventListener("scroll", navmenuScrollspy);

  ///////////////////////////////////


































  
  // Constantes del chatbot
// Constantes del chatbot
const input = document.getElementById("chat-input");
const sendBtn = document.getElementById("chat-send");
const messages = document.getElementById("chat-messages");

// Función para agregar mensajes al chat con avatar
function addMessage(text, sender) {
  const div = document.createElement("div");
  div.classList.add("message", sender);

  const avatar = document.createElement("img");
  avatar.classList.add("avatar");

  avatar.src =
    sender === "user" ? "static/img/usuario.png" : "static/img/botxd.jpg";
  avatar.alt = sender === "user" ? "Usuario" : "Chatbot";

  const messageText = document.createElement("div");
  messageText.classList.add("text");
  messageText.innerHTML = text;

  div.appendChild(avatar);
  div.appendChild(messageText);

  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

// Funciones para detectar temas específicos
function contienePalabraPromocion(texto) {
  const palabrasPromo = ["promoción", "descuento", "oferta", "cupon", "rebaja"];
  return palabrasPromo.some((palabra) => texto.includes(palabra));
}

function contienePalabraRedes(texto) {
  const palabrasRedes = [
    "redes",
    "facebook",
    "instagram",
    "whatsapp",
    "contacto",
    "twitter",
  ];
  return palabrasRedes.some((palabra) => texto.includes(palabra));
}

function contienePalabraSoporte(texto) {
  const palabrasSoporte = [
    "soporte",
    "ayuda",
    "duda",
    "problema",
    "consulta",
    "información",
    "contactar",
  ];
  return palabrasSoporte.some((palabra) => texto.includes(palabra));
}

// Función principal para obtener respuesta
async function getResponse(message) {
  const lower = message.toLowerCase();

  // Respuestas específicas antes de llamar a la IA
  if (contienePalabraPromocion(lower)) {
    return `Actualmente tenemos las siguientes promociones vigentes:<br>
    - 15% de descuento en maquinaria textil seleccionada.<br>
    - Envío gratuito para pedidos mayores a S/ 500.<br>
    - Cupones especiales para clientes recurrentes.<br>
    ¿Quieres que te ayude a aplicar alguna promoción o tienes alguna pregunta específica?`;
  }

  if (contienePalabraRedes(lower)) {
    return `Puedes seguirnos y contactarnos en nuestras redes sociales:<br>
    - Facebook: <a href="https://www.facebook.com/infotelperu" target="_blank">Infotel Perú</a><br>
    - Instagram: <a href="https://www.instagram.com/infotelperu" target="_blank">infotelperu</a><br>
    - WhatsApp: <a href="https://wa.me/51981141413" target="_blank">+51 981141413</a>`;
  }

  if (contienePalabraSoporte(lower)) {
    return `¡Hola! Soy tu asistente virtual para ayudarte con tus consultas.<br>
    Puedes preguntarme sobre:<br>
    - Información sobre nuestros productos y servicios.<br>
    - Estado de tus pedidos.<br>
    - Políticas de devolución.<br>
    - Horarios de atención.<br>
    ¿En qué puedo ayudarte hoy?`;
  }

  // Si no es ninguno de los casos anteriores, llamar a la IA
  try {
    const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
      method: "POST",
      headers: {
        Authorization:
          "Bearer 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",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        model: "deepseek/deepseek-r1-0528-qwen3-8b:free",
        messages: [{ role: "user", content: message }],
      }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data.choices[0].message.content;
  } catch (error) {
    console.error(error);
    return "Lo siento, no puedo responder ahora. Por favor intenta más tarde.";
  }
}

// Evento para enviar mensaje al hacer click
sendBtn.addEventListener("click", async () => {
  const text = input.value.trim();
  if (!text) return;
  addMessage(text, "user");
  input.value = "";

  const response = await getResponse(text);
  addMessage(response, "bot");
});

// Permitir enviar mensaje con tecla Enter
input.addEventListener("keydown", (e) => {
  if (e.key === "Enter") sendBtn.click();
});


})();
