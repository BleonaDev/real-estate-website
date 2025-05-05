document.addEventListener('DOMContentLoaded', function() {
    const searchIcon = document.getElementById('search-icon');
    const searchCon = document.getElementById('container22');
    const closeBtn = document.getElementById('close-btn');
    const searchInput = document.getElementById('search');

    searchIcon.addEventListener('click', function(event) {
        event.preventDefault();
        searchCon.style.display = 'flex';
        searchCon.style.animation = 'fadeIn 0.3s';
        searchInput.focus();
    });

    closeBtn.addEventListener('click', function() {
        searchCon.style.display = 'none';
    });
});



    new Swiper('.swiper1 .card-wrapper1', {
        loop: true,
        spaceBetween: 30,
        slidesPerView: 3,

  pagination: {
    el: '.swiper1  .swiper-pagination1',
      dynamicBullets:true,
  },

  navigation: {
    nextEl: '.swiper1 .button-next1',
    prevEl: '.swiper1  .button-prev1',
  },
});


    new Swiper('.swiper2 ', {
        effect:"coverflow",
        grabCursor:true,
        centeredSlides:true,
        initialSlide: 1,
        slidesPerView:"auto",
coverflowEffect: {
      rotate:0,
    stretch:80,
    depth:350,
    modifier:1,
    slideShadows:true,
  },
  pagination: {
    el: '.swiper-pagination2',
       dynamicBullets:true,
  },
  navigation: {
   nextEl: '.swiper2 .button-next2',
    prevEl: '.swiper2  .button-prev2',
  },
        autoplay:{
            delay:3500,
            disableOnInteraction: false,
        },
speed:700,
});

   const box = document.getElementById('luxury');

window.addEventListener('scroll', () => {
  const boxTop = box.getBoundingClientRect().top;
  const windowHeight = window.innerHeight;

  if (boxTop < windowHeight) {
    box.classList.add('visible');
  }
});

function toggleInfo() {
  var info = document.getElementById('moreInfo');
  var readMoreButton = document.getElementById('readmore');
  var readLessButton = document.getElementById('readless');

  if (getComputedStyle(info).display === "none") {
    info.style.display = "block";
    readMoreButton.style.display = "none";
    readLessButton.style.display = "inline";
  } else {
    info.style.display = "none";
    readMoreButton.style.display = "inline";
    readLessButton.style.display = "none";
  }
}




