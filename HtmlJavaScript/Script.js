
function addisjon() {
    beregn('addisjon');
}

function subtraksjon() {
    beregn('subtraksjon');
}

function multiplikasjon() {
    beregn('multiplikasjon');
}

function divisjon() {
    beregn('divisjon');
}

function beregn(operasjon) {
    var num1 = parseFloat(document.getElementById('num1').value);
    var num2 = parseFloat(document.getElementById('num2').value);
    var resultatElement = document.getElementById('resultat');

    if (isNaN(num1) || isNaN(num2)) {
        alert('Vennligst fyll inn begge tallene.');
        return;
    }

    switch (operasjon) {
        case 'addisjon':
            var resultat = num1 + num2;
            break;
        case 'subtraksjon':
            var resultat = num1 - num2;
            break;
        case 'multiplikasjon':
            var resultat = num1 * num2;
            break;
        case 'divisjon':
            if (num2 !== 0) {
                var resultat = num1 / num2;
            } else {
                alert('Kan ikke dele på null.');
                return;
            }
            break;
        default:
            alert('Ugyldig operasjon.');
            return;
    }

    resultatElement.textContent = resultat;
}
