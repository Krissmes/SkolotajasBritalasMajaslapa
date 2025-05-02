function ieladejotPievienot(saites){
    for(let objekts=1;objekts<9;objekts++){
        let lieta = document.getElementById('img'+objekts)
        console.log(objekts, "bus")
        lieta.addEventListener('click',function(eve) {
            inforadit(objekts);
        })
    }
    saitesvisas = saites;
}

var saitesvisas = [];

function dropdovnis(saitesgabals){
    let vieta = document.getElementById("infovieta");
    if(saitesgabals.length<9){
        vieta.innerHTML = "";
        return
    }
    vieta.innerHTML = "<h4>Pašlaik pievienotas saites: </h4>";
    let isais = saitesgabals.split('/')[2];
    console.log(isais);
    let nosaukums = isais.trimLeft('w');
    console.log(nosaukums);
    console.log(nosaukums.trimLeft('\W'));
    let infogabals = izlaseNoSaitem(saitesvisas,nosaukums.trimLeft('\W'));
    console.log(infogabals);
    for (let saite in infogabals){
        vieta.innerHTML = vieta.innerHTML +"</br>" + infogabals[saite];
    }
    return
}

function izlaseNoSaitem(saites,teksts){
    let rezultats = saites.filter(saite => saite.includes(teksts));
    return rezultats
}

const tabula = ["<h4>Maksa</h4></br><ul><li>Bezmaksas - viss saturs ir par brīvu</li><li>Daļēji maksas - pamatsaturs ir par brīvu, bet daļa satura/funkcionalitātes - par maksu</li></ul>",
 "<h4>Kurš veido/lieto?</h4></br><ul><li>Lieto gatavu IT resursu - nodarbībā to izmanto</li><li>Veido IT resursu - nodarbībā to veido</li><li>Mācību darbā/-am SK - resurss skolotājam</li><li>Prof. pilnveide SK - resurss skolotājam</li><li>Pirmsskolas SN - resurss  pirmskolas posma skolēnam</li><li>Sākumskolas SN - resurss sākumizglītības posma skolēnam</li><li>Pamatskolas SN - resurss pamatizglītības posma skolēnam</li><li>Vidusskola I SN - resurss vidusskolas pamatkursa skolēnam</li><li>Vidusskola II SN - resurss vidusskolas padziļinātā kursa skolēniem</li><li>Neformālā izgl. SN - Skolēniem ārpusstundu nodarbībām</li><li>Augstskola - resurss studentam</li></ul>",
"<h4>Saturs</h4></br><ul><li>Konkrēts mācību kurss <i>(Ķīmija, Bioloģija, Fizika, Ģeogrāfija, Tehnoloģijas, Matemātika, IT)</i></li><li>Dabaszinības - integrētais dabaszinātņu kurss</li><li> Dabaszinātnes - vispārīgs resurss, noderīgs daudzos mācību kursos</li><li>Mācību progr. - dota un analizēta mācību programma vai to modulis</li><li>Nodarbību plāns - dots nodarbības plāns</li><li>Metodiskais materiāls - analizēta kādas mācību stratēģijas (metodikas) izmantošana</li></ul>",
"<h4>Resursa veids</h4></br><div class='row'><div class='col'><ul><li>Zinātniskais raksts;</li><li>Uzziņām - noder informācijas atrašanai;</li><li>e-bibliotēkas - plašs resursu klāsts;</li><li>R teksts - html un cita veida teksta resurss, e-grāmata;</li><li>R grafika - vizuālā informācija: diagramma, infografika, datorprezentācija;</li><li>R skaņa - audioresurss, podkasts;</li><li> R video - arī animācija;</li><li>Virtuālā ekskursija - arī virtuālie muzeji;</li><li>Demonstrējums;</li><li>Laboratorijas darbs;</li><li>Datorizēts eksperiments - izmanto sensorus u.c. digitālās ierīces</li></ul></div><div class='col'><ul><li>Modelēšana</li><li>Simulācija - arī virtuālā laboratorija;</li><li>Spēle;</li><li>Projektu darbs;</li><li>Virtuālā tāfele;</li><li>e-portfolio - noder resursu apkopošanai, darbam ar tiem;</li><li>Jēdzienu kartes - arī domu kartes;</li><li>Kartes - arī plāni, ģeogrāfijā, astronomijā</li><li>Pamācības - teksts, video veidā;</li><li> Interaktīvs materiāls; </li><li>Uzdevums - arī tests klasē, pārbaudei;</li><li>Mācību vide</li></ul></div></div>",
"<h4>Kāpēc lieto?</h4></br><div class='row'><div class='col'><ul><li>Jauktā mācīšanās - nodarbības laikā pārmaiņus lieto IT mācību resursus un skolotāja norādes</li><li>Apvērstā mācīšanās - IT resurss tiek apgūts patstāvīgi pirms klātienes/tiešsaistes nodarbības</li><li>Mācīšanās iedziļinoties - nepieciešama domāšanas piepūle, pretstats - faktu iemācīšanās</li><li>Attālinātā mācīšanās - mācīšanās tiešsaistē</li><li> Iesaistīšana - ar to panāk, ka skolēni paši vēlas apgūt mācību saturu</li><li>Personalizēta mācīšanās - katrs apgūst mācību saturu pēc savām spējām</li><li>Balsošana- viedokļu noskaidrošana</li><li> Vērtēšana- diagnosticējošā, summatīvā</li></div><div class='col'><li>Atgriezeniskā saite - skolēnu vai skolotāja sniegta, formatīvā vērtēšana, reālajā laikā, viedokļu noskaidrošana</li><li>Pašvadīta mācīšanās - skolēns patstāvīgi organizē savu mācīšanos</li><li>Sadarbība - informācijas apmaiņa, grupu darbs mācību procesā, arī līdzatbildība</li><li>Problēmrisināšana</li><li>Zināšanu konstruēšana</li><li>Inovācijas - arī radošā jaunrade</li><li>Aktivitāte (uzdevums) klasē - uzdevums, kuru veic mācību nodarbības laikā</li><li>Mājasdarbs</li><li>Datu vākšana - internetā, eksperimenta</li><li> Datu apstrāde - analīzi, arī eksperimenta datu apstrāde, sistematizēšana</li><li> Komunikācija - arī prezentēšana</li></ul></div>",
"<h4>Mācību vides/platformas</h4></br><p>Ar šo mācību platformu (Google Classroom, MS Teams, e-klase)  pasi, var ielogoties dotajā majaslapā, bez reģistrēšanās konkrētā mājaslapā. Saiti iespējams sasaistīt ar attiecīgo mācību platformu dažādos veidos (vienota pieeja / skolēnu saraksta imports / u.c.).</p><ul><li> Interneta kopprojekti - projektu vienlaicīgi veic vairākas skolas</li><li>Skolu sadarbības tīkli - skolu sadarbības iespējas</li></ul>",
"<h4>Ar ko/kā lieto?</h4></br><ul><li>Mobilā lietotne - lai izmantotu resursu, tas  jāinstalē</li><li>Datora lietotne - lai izmantotu resursu, tas  jāinstalē</li><li>Tiešsaiste - resurss, izmantojams bez lejupielādes un instalēšanas ierīcē</li><li> Datne - var lejupielādēt ierīcē un atvērt</li><li>VR/AR - virtuālās realitātes, papildinātās realitātes resurss</li></ul>",
"<h4>Valoda</h4></br><p>Norāda IT resursa valodu.</p>"];

function inforadit(id){
    console.log(id);
    let vieta = document.getElementById("infovieta");
    vieta.innerHTML="";
    let smukumi = document.createElement("div");
    smukumi.classList.add('bg-light');
    smukumi.innerHTML=tabula[id-1];
    vieta.appendChild(smukumi);
}



