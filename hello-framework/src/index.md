---
toc: false
---

<style>
  * {
    font-family: "Gill Sans", sans-serif;
  }
  
  .hero {
    display: flex;
    flex-direction: column;
    align-items: center;
    font-family: "Gill Sans", sans-serif;
    margin: 4rem 0 8rem;
    text-wrap: balance;
    text-align: center;
  }

  .hero h1 {
    margin: 2rem 0;
    max-width: none;
    font-size: 14vw;
    font-weight: 900;
    line-height: 1;
    background: linear-gradient(30deg, var(--theme-foreground-focus), currentColor);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .hero h2 {
    margin: 0;
    max-width: none;
    font-size: 3vw;
    font-style: initial;
    font-weight: 500;
    line-height: 1;
    color: var(--theme-foreground-muted);
  }

  @media (min-width: 640px) {
    .hero h1 {
      font-size: 90px;
    }
  }

  .maplibregl-popup {
    max-width: 400px;
    font: 12px/20px 'Helvetica Neue', Arial, Helvetica, sans-serif;
  }
 .chart-container {
        max-width: 1000px; 
        margin: 0 auto; 
    }

    .chart {
        width: 100%; 
    }
    .propria{color: SpringGreen}
    .impropria{color: Crimson}
    .hidro{color: LightSeaGreen}
    .titulo{margin-top: 80px}
    .conclusao{margin-top: 80px}
</style>

<div class="hero">
  <h1>Trabalho 02</h1>
  <h2>Correlação entre balneabilidade de praias e despejo de poluentes</h2>
  <p></p>
  <h3>Gabriel Marinho, Pedro Monnerat</h3>
</div>
<h2 class="titulo">Pontos de Balneabilidade</h2>
<p>Para essa visualização decidimos utilizar canais visuais com marcadores circulares expressivos e efetivos, utilizando cores intuitivas e semanticamente diferentes, facilitando a percepção.</p><p>Escolhemos representar dados geográficos através do mapa, que auxilia na vizualização, pois deixa mais intuitiva a inferência de que áreas poluídas têm correlação com pontos de escoamento.</p> <p>O público alvo que seria a população de Niteroi possui familiaridade com os locais.</p>
<ul><h4>Legenda:</h4>
<li><div class="impropria"><b>Ponto vermelho:</b></div> Praia Imprópira para banho</li>
<li><div class="propria"><b>Ponto verde:</b></div> Praia Própira para banho</li>
<li><div class="hidro"><b>Linhas Azuis:</b></div> Rotas de escoamento da hidrografia</li>
</ul>
<p>É possível fazer interações de navegação para obter mais detalhes.</p> 
<div id="info" style="width: 100%; margin-top: 15px;">
  <h3 class="title">Clique em qualquer ponto para Informações</h3>
  <div id="info-content"></div>
</div>
<div style="width: 100%; height: 500px; margin-top: 15px;">
  <div id="ex03" style="width: 100%; height: 430px; margin-top: 15px;"></div>
</div>


<h2> Análise das informações da visualização</h2>
<p>Nessa extração mais recente dos dados, podemos perceber que todos os pontos impróprios para banho encontram-se dentro da Baía de Guanabara. Nota-se também que os locais com pontos vermelhos em sua maioria estão próximos de saídas de escoamento hidrográfico, representados pelas pontas das linhas azuis, que desaguam na Baía.</p><p>Podemos ver que na região oceânica, não há saídas de escoamento hidrográfico nas praias. Na vizualização, todos os pontos de balneabilidade oceânicos estão próprios.</p><p>Logo, infere-se que existe uma correlação entre o despejo hidrográfico e a balneabilidade desses pontos. Sabemos que o despejo pode trazer muitos poluentes, causando problemas para a biodiversidade dos locais afetados, além de torná-los infrequentáveis.</p><p>Apesar dessa vizualização representar apenas dados relativos a um determinado momento no tempo, podemos afirmar que esse cenário é bastante comum, conforme veremos na seguinte visualização.</p>



<h2 class="titulo">Distribuição anual de pontos por localização da praia</h2>
<p>Para essa visualização, escolhemos um gráfico de barras empilhadas comparativo. Utilizamos dados geográficos relacionados à região em que as praias se localizam, a partir de dados temporais agrupados dos últimos 5 anos.</p><p>O valor dos pontos de balneabilidade utilizado na vizualização foi a soma das ocorrências de balneabilidade impróprias e Próprias. Os valores de cada ano são mapeados ao tamanho das barras.</p> <p>Os dados geográficos estão representados a partir do canal visual de cores harmoniosas e semanticamente distintas, que diferenciam cada região.</p>
<div id="ex04" class="card">
    <div class="chart-container">
            ${ vl.render(ex04(divWidth - 70)) }
        </div>
</div>
<div id="ex04" class="card">
    <div class="chart-container">
            ${ vl.render(ex05(divWidth - 70)) }
        </div>
</div>
<h2> Análise das informações da visualização</h2>
<p>Nessa segunda vizualização, temos a disposição dados referentes aos últimos 5 anos, representando a quantidade de pontos de balnebilidade imprópria e própria de cada região.</p><p>Imediatamente, podemos perceber a diferença volumosa entre as duas regiões.</p><p>Em todos os 5 anos analisados, as praias da Baía tiveram número excessivamente maior de ocorrências de águas impróprias em relação às praias oceânicas.</p><p>Assim, fica claro que a maior ocorrência de águas poluídas na Baía de Guanabara não é um evento isolado, mas sim uma realidade recorrente.</p><p>Percebe-se também que o números de ocorrências de balneabilidade própria ainda é maior na região oceânica, mas não tão expressivamente quanto o número de impróprias. Isso pode ser visto no mapa, já que nem todos os pontos da Baía estão impróprios, mostrando que é possível manter a qualidade da água em locais afastados de despejos.</p>

<div class="conclusao">
<h3>Conclusão</h3>
<p>Vimos que o despejo de poluentes está profundamente relacionado à poluição das águas. Esse despejo bota cada vez mais em risco a biodiversidade e a saúde dos frequentadores desses pontos afetados.</p>
<p>Seria interessante a realização de estudos para implantação de alternativas a esse descarte danoso, visto que a causa do problema é tão evidente e identificável, como foi apresentado nessa visualização.</p>
<ul><h4>Fontes de Dados: Prefeitura de Niterói (SIGeo)</h4>
<li><a href="https://www.sigeo.niteroi.rj.gov.br/datasets/39ed61e15ea14c1281ea60e0e16cb071_60/explore">Hidrografia</a></li>
<li><a href="https://www.sigeo.niteroi.rj.gov.br/datasets/geoniteroi::pontos-de-balneabilidade/explore?layer=0">Pontos de Balneabilidade</a></li>
<li><a href="https://www.sigeo.niteroi.rj.gov.br/datasets/geoniteroi::pontos-de-balneabilidade/explore?layer=1">Histórico de Balneabilidade
</a></li>
</ul>
</div>

```js
const pontosBal = await FileAttachment("./data/Pontos_de_Balneabilidade.geojson").json({typed: true});
const hidro = await FileAttachment("./data/Hidrografia.geojson").json({typed: true});
const bairros = await FileAttachment("./data/mapBairros.csv").csv({typed: true});
const ocorrencias = await FileAttachment("./data/ocorrAno.csv").csv({typed: true});

```

```js
const divWidth = Generators.width(document.querySelector("#ex04"));

const divWidth03 = Generators.width(document.querySelector("#ex03"));


```

```js
import * as vega from "npm:vega";
import * as vegaLite from "npm:vega-lite";
import * as vegaLiteApi from "npm:vega-lite-api";
import maplibregl from "npm:maplibre-gl";

const vl = vegaLiteApi.register(vega, vegaLite);

function ex03() {
    const map01 = document.querySelector("#ex03");
    map01.style.width = `${divWidth03}px`;
    map01.style.height = '400px';

    const map = new maplibregl.Map({
        container: map01,
        style: "https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json",
        center: [-43.1227, -22.9295],
        zoom: 11,
    });

    map.on("load", function () {
        map.addSource("pontos", {
            type: "geojson",
            data: pontosBal,
        });
        map.addSource("hidrografia", {
            type: "geojson",
            data: hidro,
        });
        map.addLayer({
            id: "pontos-layer",
            type: "circle",
            source: "pontos",
            paint: {
                "circle-color": [
                    "match",
                    ["get", "tx_status"],
                    "Própria", "SpringGreen",
                    "Imprópria", "Crimson",
                    "#0000FF"
                ],
                "circle-radius": 6,
                "circle-stroke-color": [
                    "match",
                    ["get", "tx_status"],
                    "Própria", "SeaGreen",
                    "Imprópria", "Maroon",
                    "#0000FF"
                ],
                "circle-stroke-width": 1,
            }
        });
        map.addLayer({
            id: "hidro-layer",
            type: "line",
            source: "hidrografia",
            paint: {
                "line-color": "LightSeaGreen",
                "line-width": 3
            }
        });

        map.on('mouseenter', 'pontos-layer', function () {
            map.getCanvas().style.cursor = 'pointer';
        });

        map.on('mouseleave', 'pontos-layer', function () {
            map.getCanvas().style.cursor = '';
        });

        map.on('click', 'pontos-layer', function (e) {
            map.getCanvas().style.cursor = 'pointer';

            const coordinates = e.features[0].geometry.coordinates.slice();
            const tx_localizacao = e.features[0].properties.tx_localizacao;
            const tx_status = e.features[0].properties.tx_status;
            const dt_dtatualizacao = e.features[0].properties.dt_dtatualizacao;
            const tx_codptcoleta = e.features[0].properties.tx_codptcoleta;
            const tx_praia = e.features[0].properties.tx_praia;

            document.getElementById('info-content').innerHTML = `
                <strong>Ponto de Balneabilidade: ${tx_localizacao}</strong><br>
                <table>
                    <tr><th>Data de Atualização</th><td>${new Date(dt_dtatualizacao).toLocaleString()}</td></tr>
                    <tr><th>Localização</th><td>${tx_localizacao}</td></tr>
                    <tr><th>Ponto de Coleta</th><td>${tx_codptcoleta}</td></tr>
                    <tr><th>Status da Praia</th><td>${tx_status}</td></tr>
                </table>
            `;
        });
    });

    map.on('idle', function () {
        map.resize();
    });

    invalidation.then(() => map.remove());
}

ex03();

function ex04(divWidth) {
    return {
        "spec": {
            "width": divWidth - 200,
            "height": 300, 
            "data": {
                "values": ocorrencias
            },
            "transform": [
                {"filter": "datum.tx_status === 'Imprópria'"}
            ],
            "background": "#101010",
            "mark": {
                "type": "bar",
                "tooltip": true,
            },
            "encoding": {
                "x": {
                    "field": "ano",
                    "type": "ordinal",
                    "axis": {"title": "Ano", "labelColor": "white", "labelAngle": 0,} 
                },
                "y": {
                    "title": "Quantidade de Praias Impróprias",
                    "aggregate": "sum",
                    "field": "quantidade",
                    "type": "quantitative",
                    "axis": {"labelColor": "white"} 
                },
                "color": {
                    "field": "tipo",
                    "type": "nominal",
                    "scale": {
                        "domain": ["Baía de Guanabara", "Oceânica"],
                        "range": ["#483D8B", "#6495ED"],
                    },
                    "legend": {"title": "Tipo de Praia", "labelColor": "white", "titleColor": "white"}, 
                }
            },
            "config": {
                "axis": {
                    "titleColor": "white", 
                    "labelColor": "white"  
                }
            }
        }
    };
}

function ex05(divWidth) {
    return {
        "spec": {
            "width": divWidth - 200,
            "height": 300, 
            "data": {
                "values": ocorrencias
            },
            "transform": [
                {"filter": "datum.tx_status === 'Própria'"}
            ],
            "background": "#101010",
            "mark": {
                "type": "bar",
                "tooltip": true,
            },
            "encoding": {
                "x": {
                    "field": "ano",
                    "type": "ordinal",
                    "axis": {"title": "Ano", "labelColor": "white", "labelAngle": 0,} 
                },
                "y": {
                    "title": "Quantidade de Praias Próprias",
                    "aggregate": "sum",
                    "field": "quantidade",
                    "type": "quantitative",
                    "axis": {"labelColor": "white"} 
                },
                "color": {
                    "field": "tipo",
                    "type": "nominal",
                    "scale": {
                        "domain": ["Baía de Guanabara", "Oceânica"],
                        "range": ["#483D8B", "#6495ED"],
                    },
                    "legend": {"title": "Tipo de Praia", "labelColor": "white", "titleColor": "white"}, 
                }
            },
            "config": {
                "axis": {
                    "titleColor": "white", 
                    "labelColor": "white"  
                }
            }
        }
    };
}

```