fetch('assets/data/courses.json')
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById('courses-container');
    if (!container) return;

    container.innerHTML = '';

    data.courses.forEach(course => {
      container.innerHTML += `
        <div class="col-lg-4 col-md-6">
          <div class="properties pb-20">
            <div class="properties__card">
              <div class="properties__img overlay1">
                <img src="${course.image}" loading="lazy">
              </div>
              <div class="properties__caption">
                <p>${course.category}</p>
                <h3>${course.title}</h3>
                <p>${course.description}</p>
                <div class="price">
                  <span>${course.price}</span>
                </div>
                <a href="${course.whatsapp}" target="_blank" class="border-btn border-btn2">
                  Enroll Now
                </a>
              </div>
            </div>
          </div>
        </div>
      `;
    });
  });