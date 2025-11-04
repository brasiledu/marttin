// JavaScript da Landing Page - Marttin AI
// High-performance optimized JavaScript
(function() {
    'use strict';
    
    // Performance optimizations
    const passiveOptions = { passive: true };
    let rafId;
    
    // Debounced scroll handler
    let scrollTimeout;
    function debounce(func, wait) {
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(scrollTimeout);
                func(...args);
            };
            clearTimeout(scrollTimeout);
            scrollTimeout = setTimeout(later, wait);
        };
    }
    
    // Smooth scrolling for navigation links (optimized)
    document.addEventListener('click', function(e) {
        const anchor = e.target.closest('a[href^="#"]');
        if (anchor) {
            e.preventDefault();
            const target = document.querySelector(anchor.getAttribute('href'));
            if (target) {
                if (rafId) cancelAnimationFrame(rafId);
                rafId = requestAnimationFrame(() => {
                    target.scrollIntoView({ 
                        behavior: 'smooth', 
                        block: 'start' 
                    });
                });
            }
        }
    }, passiveOptions);

    // Highly optimized Intersection Observer
    const observerOptions = {
        threshold: [0, 0.1],
        rootMargin: '0px 0px -50px 0px'
    };

    const animationObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting && entry.intersectionRatio > 0) {
                requestAnimationFrame(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                    setTimeout(() => {
                        entry.target.style.willChange = 'auto';
                    }, 600);
                });
                animationObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Batch DOM operations for better performance
    const elementsToAnimate = document.querySelectorAll('.feature-card, .pricing-card');
    
    requestAnimationFrame(() => {
        elementsToAnimate.forEach(card => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(50px)';
            card.style.transition = 'transform 0.6s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.6s ease';
            card.style.willChange = 'transform, opacity';
            animationObserver.observe(card);
        });
    });

    // Special observer for laptop mockup with optimized timing
    const laptop = document.querySelector('.laptop-mockup');
    if (laptop) {
        requestAnimationFrame(() => {
            laptop.style.opacity = '0';
            laptop.style.transform = 'perspective(1000px) rotateY(-15deg) translateY(50px)';
            laptop.style.transition = 'all 0.8s cubic-bezier(0.4, 0, 0.2, 1)';
            laptop.style.willChange = 'transform, opacity';
            animationObserver.observe(laptop);
        });
    }

    // Highly optimized CTA button interactions
    const ctaButtonsMap = new WeakMap();
    document.addEventListener('mouseenter', function(e) {
        const button = e.target.closest('.cta-button');
        if (button && !ctaButtonsMap.has(button)) {
            ctaButtonsMap.set(button, true);
            requestAnimationFrame(() => {
                button.style.transform = 'translateY(-3px) scale(1.05)';
            });
        }
    }, passiveOptions);
    
    document.addEventListener('mouseleave', function(e) {
        const button = e.target.closest('.cta-button');
        if (button && ctaButtonsMap.has(button)) {
            ctaButtonsMap.delete(button);
            requestAnimationFrame(() => {
                button.style.transform = 'translateY(-3px) scale(1)';
            });
        }
    }, passiveOptions);

    // Optimized carousel functionality with content switching
    const carouselDots = document.querySelectorAll('.carousel-dot');
    const dashboardViews = document.querySelectorAll('.dashboard-view');
    let currentSlide = 2;
    
    if (carouselDots.length > 0 && dashboardViews.length > 0) {
        // Function to switch dashboard view
        function switchDashboard(index) {
            if (index === currentSlide) return;
            
            requestAnimationFrame(() => {
                // Hide current
                dashboardViews[currentSlide].classList.remove('active');
                carouselDots[currentSlide].classList.remove('active');
                
                // Show new
                dashboardViews[index].classList.add('active');
                carouselDots[index].classList.add('active');
                
                currentSlide = index;
            });
        }
        
        // Event delegation for carousel dots
        document.addEventListener('click', function(e) {
            const dot = e.target.closest('.carousel-dot');
            if (dot) {
                const index = Array.from(carouselDots).indexOf(dot);
                if (index !== -1) {
                    switchDashboard(index);
                }
            }
        });

        // Auto-rotate with optimized timing
        setInterval(() => {
            const nextSlide = (currentSlide + 1) % dashboardViews.length;
            switchDashboard(nextSlide);
        }, 5000);
    }

    // Optimized pricing button interactions with event delegation
    document.addEventListener('click', function(e) {
        const planButton = e.target.closest('.plan-button');
        if (planButton) {
            console.log('Plano selecionado');
            // TODO: Integração com sistema de pagamento
        }
    });

    // Performance monitoring and optimization
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        // Desabilitar animações para usuários que preferem movimento reduzido
        document.querySelectorAll('*').forEach(el => {
            el.style.animation = 'none';
            el.style.transition = 'none';
        });
    }

    // Clean up on page unload
    window.addEventListener('beforeunload', () => {
        animationObserver.disconnect();
    }, passiveOptions);

    // Optimize for high refresh rate displays
    let lastTime = 0;
    function optimizedRAF(callback) {
        const currentTime = Date.now();
        const timeToCall = Math.max(0, 16 - (currentTime - lastTime));
        const id = setTimeout(() => callback(currentTime + timeToCall), timeToCall);
        lastTime = currentTime + timeToCall;
        return id;
    }

    // Preload critical elements for smoother experience
    requestIdleCallback(() => {
        // Preload images that might be needed
        const criticalImages = document.querySelectorAll('img[data-preload]');
        criticalImages.forEach(img => {
            const preloadLink = document.createElement('link');
            preloadLink.rel = 'preload';
            preloadLink.as = 'image';
            preloadLink.href = img.src;
            document.head.appendChild(preloadLink);
        });
    });

})();