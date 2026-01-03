function toggleMenu() {
  const menu = document.getElementById("mobileMenu");
  menu.style.display = menu.style.display === "flex" ? "none" : "flex";
}

  const counters = document.querySelectorAll('.counter');

  counters.forEach(counter => {
    const updateCount = () => {
      const target = +counter.getAttribute('data-target');
      const count = +counter.innerText;
      const speed = 200; // lower = faster

      const increment = Math.ceil(target / speed);

      if (count < target) {
        counter.innerText = count + increment;
        setTimeout(updateCount, 30);
      } else {
        counter.innerText = target + "+";
      }
    };

    updateCount();
  });









const cards = document.querySelectorAll(".gallery-card");
const lightbox = document.getElementById("lightbox");
const imgBox = document.getElementById("lightbox-img");
const videoBox = document.getElementById("lightbox-video");

cards.forEach(card => {
  card.onclick = () => {
    lightbox.style.display = "flex";

     // Pause all grid videos
    document.querySelectorAll(".gallery-card video").forEach(v => v.pause());

    if (card.classList.contains("video")) {
      imgBox.style.display = "none";
      videoBox.style.display = "block";
      videoBox.src = card.querySelector("video source").src;
      videoBox.currentTime = 0;
      videoBox.play();
    } else {
      videoBox.style.display = "none";
      imgBox.style.display = "block";
      imgBox.src = card.querySelector("img").src;
    }
  };
});

document.querySelector(".close").onclick = () => {
  lightbox.style.display = "none";
  videoBox.pause();
};


