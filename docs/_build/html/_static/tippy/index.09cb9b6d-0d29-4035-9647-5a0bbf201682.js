selector_to_html = {"a[href=\"#fundamentals-of-astronomy-and-astrophysics\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Fundamentals of Astronomy and Astrophysics<a class=\"headerlink\" href=\"#fundamentals-of-astronomy-and-astrophysics\" title=\"Link to this heading\">#</a></h1><h2>Notes of the course for the Bachelor\u2019s degree in Aerospace Engineering<a class=\"headerlink\" href=\"#notes-of-the-course-for-the-bachelors-degree-in-aerospace-engineering\" title=\"Link to this heading\">#</a></h2><p><img alt=\"Degree\" src=\"https://img.shields.io/badge/Degree-Aerospace%20Engineering-8A2BE2\"/>\n<img alt=\"Course\" src=\"https://img.shields.io/badge/Course-Fundamentals%20of%20Astronomy%20and%20Astrophysics-violet\"/>\n<a class=\"reference external\" href=\"https://github.com/LucaMalavolta/Notes_FAandA\"><img alt=\"GitHub\" src=\"https://img.shields.io/badge/GitHub-FAandA-blue\"/></a></p><p>Edit directly on GitHub page</p>", "a[href=\"chapter01_spherical_astronomy.html\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Spherical Astronomy<a class=\"headerlink\" href=\"#spherical-astronomy\" title=\"Link to this heading\">#</a></h1><h2>The Celestial Sphere<a class=\"headerlink\" href=\"#the-celestial-sphere\" title=\"Link to this heading\">#</a></h2><p>Historically speaking, the <strong>Celestial Sphere</strong> was the apparent surface of the heavens, on which the stars seem to be fixed.\nNowadays, the term <em>Celestial sphere</em> refers to an abstract construct used to describe the locations of objects in the sky.</p><p>The Celestial Sphere has an infinite radius, in the sense that all the objects on it are at the same endless distance. In other words, the distance of an object is not required to describe its position in the sky. For obvious mathematical reasons, it is easier to deal with a sphere with a <em>unitary</em> radius (think about trigonometry) rather than an infinite one. The centre of the Earth is the centre of the celestial sphere, and the sphere\u2019s pole and equatorial plane are coincident with those of the Earth.</p>", "a[href=\"#table-of-contents\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Table of contents<a class=\"headerlink\" href=\"#table-of-contents\" title=\"Link to this heading\">#</a></h2><p><a class=\"reference external\" href=\"https://www.python.org/\"><img alt=\"forthebadge made-with-python\" src=\"http://ForTheBadge.com/images/badges/made-with-python.svg\"/></a></p><p>This documentation has been rendered using the <a class=\"reference external\" href=\"https://sphinx-book-theme.readthedocs.io/\">Sphinx Book Theme</a> and the <a class=\"reference external\" href=\"https://myst-parser.readthedocs.io/\">Myst parser</a></p>", "a[href=\"#notes-of-the-course-for-the-bachelors-degree-in-aerospace-engineering\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Notes of the course for the Bachelor\u2019s degree in Aerospace Engineering<a class=\"headerlink\" href=\"#notes-of-the-course-for-the-bachelors-degree-in-aerospace-engineering\" title=\"Link to this heading\">#</a></h2><p><img alt=\"Degree\" src=\"https://img.shields.io/badge/Degree-Aerospace%20Engineering-8A2BE2\"/>\n<img alt=\"Course\" src=\"https://img.shields.io/badge/Course-Fundamentals%20of%20Astronomy%20and%20Astrophysics-violet\"/>\n<a class=\"reference external\" href=\"https://github.com/LucaMalavolta/Notes_FAandA\"><img alt=\"GitHub\" src=\"https://img.shields.io/badge/GitHub-FAandA-blue\"/></a></p><p>Edit directly on GitHub page</p>"}
skip_classes = ["headerlink", "sd-stretched-link"]

window.onload = function () {
    for (const [select, tip_html] of Object.entries(selector_to_html)) {
        const links = document.querySelectorAll(` ${select}`);
        for (const link of links) {
            if (skip_classes.some(c => link.classList.contains(c))) {
                continue;
            }

            tippy(link, {
                content: tip_html,
                allowHTML: true,
                arrow: true,
                placement: 'auto-start', maxWidth: 500, interactive: false,

            });
        };
    };
    console.log("tippy tips loaded!");
};
