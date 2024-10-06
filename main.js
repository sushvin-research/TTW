document.querySelectorAll('p').forEach(p => {
    if (p.textContent.startsWith('Day') && p.querySelector('strong')) {
        p.style.textAlign = 'center';
    }
});