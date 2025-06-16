# JavaScript Guide - Landing Page

## Arquitetura JavaScript

### Estrutura Geral
```javascript
(function() {
    'use strict';
    
    // 1. Configurações e constantes
    // 2. Utility functions
    // 3. Performance optimizations
    // 4. Event handlers
    // 5. Observers e animations
    // 6. Component functionality
    // 7. Cleanup
    
})();
```

## Performance Optimizations

### Event Delegation
```javascript
// ❌ Evitar - Múltiplos event listeners
const buttons = document.querySelectorAll('.btn');
buttons.forEach(btn => {
    btn.addEventListener('click', handleClick);
});

// ✅ Usar - Event delegation
document.addEventListener('click', function(e) {
    const button = e.target.closest('.btn');
    if (button) {
        handleClick(e, button);
    }
}, { passive: true });
```

### RequestAnimationFrame
```javascript
// ❌ Evitar - Direct DOM manipulation
element.style.transform = 'translateY(-10px)';

// ✅ Usar - RequestAnimationFrame
let rafId;
function smoothTransform(element, transform) {
    if (rafId) cancelAnimationFrame(rafId);
    rafId = requestAnimationFrame(() => {
        element.style.transform = transform;
    });
}
```

### Debouncing
```javascript
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Usage
const debouncedScroll = debounce(handleScroll, 100);
window.addEventListener('scroll', debouncedScroll, { passive: true });
```

### Passive Event Listeners
```javascript
const passiveOptions = { passive: true };

// Para eventos que não precisam de preventDefault()
document.addEventListener('scroll', handleScroll, passiveOptions);
document.addEventListener('touchstart', handleTouch, passiveOptions);
```

## Intersection Observer

### Animation Observer
```javascript
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
                
                // Cleanup will-change after animation
                setTimeout(() => {
                    entry.target.style.willChange = 'auto';
                }, 600);
            });
            
            // Stop observing after animation
            animationObserver.unobserve(entry.target);
        }
    });
}, observerOptions);

// Apply to elements
const elementsToAnimate = document.querySelectorAll('.feature-card, .pricing-card');
elementsToAnimate.forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(50px)';
    card.style.transition = 'transform 0.6s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.6s ease';
    card.style.willChange = 'transform, opacity';
    animationObserver.observe(card);
});
```

### Lazy Loading Observer
```javascript
const lazyImageObserver = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;
            img.classList.remove('lazy');
            lazyImageObserver.unobserve(img);
        }
    });
});

// Apply to lazy images
document.querySelectorAll('img[data-src]').forEach(img => {
    lazyImageObserver.observe(img);
});
```

## Carousel Functionality

### Core Carousel Logic
```javascript
class DashboardCarousel {
    constructor() {
        this.carouselDots = document.querySelectorAll('.carousel-dot');
        this.dashboardViews = document.querySelectorAll('.dashboard-view');
        this.currentSlide = 2; // Start at third slide
        this.autoRotateInterval = null;
        
        this.init();
    }
    
    init() {
        if (this.carouselDots.length > 0 && this.dashboardViews.length > 0) {
            this.bindEvents();
            this.startAutoRotate();
            this.switchDashboard(this.currentSlide); // Set initial state
        }
    }
    
    bindEvents() {
        // Event delegation for dots
        document.addEventListener('click', (e) => {
            const dot = e.target.closest('.carousel-dot');
            if (dot) {
                const index = Array.from(this.carouselDots).indexOf(dot);
                if (index !== -1) {
                    this.switchDashboard(index);
                    this.resetAutoRotate();
                }
            }
        });
    }
    
    switchDashboard(index) {
        // Remove active class from all
        this.dashboardViews.forEach(view => view.classList.remove('active'));
        this.carouselDots.forEach(dot => dot.classList.remove('active'));
        
        // Add active class to selected
        if (this.dashboardViews[index]) {
            this.dashboardViews[index].classList.add('active');
        }
        if (this.carouselDots[index]) {
            this.carouselDots[index].classList.add('active');
        }
        
        this.currentSlide = index;
    }
    
    startAutoRotate() {
        this.autoRotateInterval = setInterval(() => {
            requestAnimationFrame(() => {
                const nextSlide = (this.currentSlide + 1) % this.carouselDots.length;
                this.switchDashboard(nextSlide);
            });
        }, 5000);
    }
    
    resetAutoRotate() {
        clearInterval(this.autoRotateInterval);
        this.startAutoRotate();
    }
    
    destroy() {
        clearInterval(this.autoRotateInterval);
    }
}

// Initialize carousel
const carousel = new DashboardCarousel();
```

## Smooth Scrolling

### Anchor Link Handling
```javascript
function initSmoothScrolling() {
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
    }, { passive: true });
}
```

### Intersection Observer for Navigation
```javascript
function initNavigationHighlight() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('a[href^="#"]');
    
    const navObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Update active nav link
                navLinks.forEach(link => link.classList.remove('active'));
                const activeLink = document.querySelector(`a[href="#${entry.target.id}"]`);
                if (activeLink) {
                    activeLink.classList.add('active');
                }
            }
        });
    }, {
        threshold: 0.3,
        rootMargin: '-100px 0px -100px 0px'
    });
    
    sections.forEach(section => navObserver.observe(section));
}
```

## Button Interactions

### CTA Button Effects
```javascript
function initButtonEffects() {
    const ctaButtonsMap = new WeakMap();
    
    // Hover effects
    document.addEventListener('mouseenter', function(e) {
        const button = e.target.closest('.cta-button');
        if (button && !ctaButtonsMap.has(button)) {
            ctaButtonsMap.set(button, true);
            requestAnimationFrame(() => {
                button.style.transform = 'translateY(-3px) scale(1.05)';
            });
        }
    }, { passive: true });
    
    document.addEventListener('mouseleave', function(e) {
        const button = e.target.closest('.cta-button');
        if (button && ctaButtonsMap.has(button)) {
            ctaButtonsMap.delete(button);
            requestAnimationFrame(() => {
                button.style.transform = 'translateY(-3px) scale(1)';
            });
        }
    }, { passive: true });
    
    // Click effects
    document.addEventListener('click', function(e) {
        const planButton = e.target.closest('.plan-button');
        if (planButton) {
            e.preventDefault();
            
            // Visual feedback
            planButton.style.transform = 'scale(0.95)';
            requestAnimationFrame(() => {
                setTimeout(() => {
                    planButton.style.transform = '';
                }, 150);
            });
        }
    });
}
```

## Performance Monitoring

### Frame Rate Optimization
```javascript
let lastTime = 0;
function optimizedRAF(callback) {
    return requestAnimationFrame((time) => {
        if (time - lastTime >= 16.67) { // Cap at 60fps
            lastTime = time;
            callback(time);
        } else {
            requestAnimationFrame(() => optimizedRAF(callback));
        }
    });
}
```

### Memory Management
```javascript
const elementCache = new WeakMap();
const animationIds = new Set();

function cleanupAnimation(id) {
    if (animationIds.has(id)) {
        cancelAnimationFrame(id);
        animationIds.delete(id);
    }
}

function addAnimation(callback) {
    const id = requestAnimationFrame(callback);
    animationIds.add(id);
    return id;
}
```

### Reduced Motion Support
```javascript
function handleReducedMotion() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        // Disable heavy animations
        document.documentElement.style.setProperty('--animation-duration', '0.2s');
        
        const elementsToAnimate = document.querySelectorAll('.animated-element');
        elementsToAnimate.forEach(el => {
            el.style.transition = 'opacity 0.2s ease';
        });
    }
}
```

## Error Handling

### Safe DOM Queries
```javascript
function safeQuerySelector(selector) {
    try {
        return document.querySelector(selector);
    } catch (error) {
        console.warn(`Invalid selector: ${selector}`, error);
        return null;
    }
}

function safeQuerySelectorAll(selector) {
    try {
        return document.querySelectorAll(selector);
    } catch (error) {
        console.warn(`Invalid selector: ${selector}`, error);
        return [];
    }
}
```

### Feature Detection
```javascript
function hasFeatureSupport() {
    return {
        intersectionObserver: 'IntersectionObserver' in window,
        requestAnimationFrame: 'requestAnimationFrame' in window,
        backdrop: CSS.supports('backdrop-filter', 'blur(10px)'),
        customProperties: CSS.supports('color', 'var(--test)'),
        grid: CSS.supports('display', 'grid')
    };
}

const features = hasFeatureSupport();
if (!features.intersectionObserver) {
    // Fallback for animation triggers
    window.addEventListener('scroll', debounce(checkElementsInView, 100));
}
```

## Cleanup and Memory Management

### Page Unload Cleanup
```javascript
function initCleanup() {
    window.addEventListener('beforeunload', () => {
        // Cancel all pending animations
        animationIds.forEach(id => cancelAnimationFrame(id));
        animationIds.clear();
        
        // Clear all timers
        if (scrollTimeout) clearTimeout(scrollTimeout);
        
        // Disconnect observers
        if (animationObserver) animationObserver.disconnect();
        if (lazyImageObserver) lazyImageObserver.disconnect();
        
        // Cleanup carousel
        if (carousel) carousel.destroy();
        
    }, { passive: true });
}
```

### Idle Callback Optimizations
```javascript
function initIdleOptimizations() {
    if ('requestIdleCallback' in window) {
        requestIdleCallback(() => {
            // Preload critical elements when browser is idle
            const heavyElements = document.querySelectorAll('.dashboard-mockup, .laptop-mockup');
            heavyElements.forEach(el => {
                // Force style calculation during idle time
                el.style.transform = el.style.transform;
            });
        });
    }
}
```

## Testing Utilities

### Performance Testing
```javascript
function measurePerformance(name, fn) {
    const start = performance.now();
    const result = fn();
    const end = performance.now();
    console.log(`${name}: ${end - start}ms`);
    return result;
}

// Usage
measurePerformance('Carousel Switch', () => {
    carousel.switchDashboard(2);
});
```

### Debug Mode
```javascript
const DEBUG = false; // Set to true for development

function debugLog(...args) {
    if (DEBUG) {
        console.log('[Landing Page Debug]:', ...args);
    }
}

function debugElement(element, action) {
    if (DEBUG && element) {
        console.log(`[Element ${action}]:`, element, {
            visible: element.offsetParent !== null,
            rect: element.getBoundingClientRect(),
            styles: getComputedStyle(element)
        });
    }
}
```

## Complete Initialization
```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all functionality
    initSmoothScrolling();
    initNavigationHighlight();
    initButtonEffects();
    handleReducedMotion();
    initCleanup();
    initIdleOptimizations();
    
    // Initialize carousel
    const carousel = new DashboardCarousel();
    
    debugLog('Landing page initialized');
});
```
