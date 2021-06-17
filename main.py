from docxtpl import DocxTemplate
import math

doc = DocxTemplate("Memoria de cálculos del estribo cim profunda.docx")

def design(params):
    # params: parámetros del diseño
    # fc_estribo: resistencia del concreto estribo, MPa
    # fc_supeestructura: resistencia del concreto de la superestructura, MPa
    # E_acero: Módulo de elasticidad del acero, MPa
    # numero_carriles: número de carriles en el puente


    #Datos de entrada
    fc_estribo = params['fc_estribo'] = params.get('fc_estribo', 21)

    fc_superestructura = params['fc_superestructura'] = params.get('fc_superestructura', 28)
    
    E_acero = params['E_acero'] = params.get('E_acero', 200000)

    fy = params['fy'] = params.get('fy', 420)

    numero_carriles = params['numero_carriles'] = params.get('numero_carriles', 4)

    #Materiales

    # pesoespecifico_concreto: Peso especifico del concreto, kN/m3
    # pesoespecifico_carpetaasfaltica: Peso especifico de la carpeta asfaltica, kN/m3

    pesoespecifico_concreto = params['pesoespecifico_concreto'] = params.get('pesoespecifico_concreto', 23.544)

    pesoespecifico_carpetaasfaltica = params['pesoespecifico_carpetaasfaltica'] = params.get('pesoespecifico_carpetaasfaltica', 21.582)

    ## Información estudio de suelos
    # tipodesuelo: tipo de suelo definidos en CCP-14, Figuras 11.6.3.2-1 y 11.6.3.2-2
    # pesoespecifico_suelo: peso específico del suelo, kN/m3
    # capacidaddecarganominaldelsuelo: capacidad de carga nominal del suelo, MPa, Art. 10.6.3
    # angulodefriccioninternadelsueloconcreto: ángulo de friccion del suelo y el conreto, Art 3.11.5.3-1, Grados
    # angulodefriccioninternadelsuelorelleno: ángulo de fricción interna del suelo de relleno, Grados.
    # perfildelsuelo: Perfil del suelo, Tabla 3.10.3.1
    
    tipodesuelo = params['tipodesuelo'] = 'no rocoso'

    pesoespecifico_suelo = params['pesoespecifico_suelo'] = params.get('pesoespecifico_suelo', 18.639) 

    #capacidaddecarganominaldelsuelo = params['capacidaddecarganominaldelsuelo'] = params.get('capacidaddecarganominaldelsuelo', 1)

    angulodefricciondelsueloconcreto = params['angulodefricciondelsueloconcreto'] = params.get('angulodefricciondelsueloconcreto', 17)

    perfildelsuelo = params['perfildelsuelo'] = 'Perfil C'

    angulodefriccioninternadelsuelorelleno = params['angulodefriccioninternadelsuelorelleno'] = params.get('angulodefriccioninternadelsuelorelleno', 30)

    ## Estados limite 

    #Estado limite de resistencia
    # factorderesistencia_punta_resistencia: factor de resistencia por punta especificado en la Tabla 10.5.5.2.4-1 para el estado de límite resistencia.
    # factorderesistencia_friccion_resistencia: factor de resistencia por fricción especificado en la Tabla 10.5.5.2.4-1 para el estado de límite resistencia
    # factorderesistencia_punta_servicio: factor de resistencia por punta especificado en la Tabla 10.5.5.1 para el estado límite de servicio
    # factorderesistencia_friccion_servicio: factor de resistencia por fricción especificado en la Tabla 10.5.5.1 para el estado límite de servicio
    # factorderesistencia_punta_eventoextremo: factor de resistencia por punta especificado en la Tabla 10.5.5.3.3 para el estado límite de evento extremo
    # factorderesistencia_friccion_eventoextremo: factor de resistencia por fricción especificado en la Tabla 10.5.5.3.3 para el estado límite de evento extremo
    
    # factorderesistencia_friccion_levantamiento: factor de resistencia por fricción especificado en la Tabla 10.5.5.3.2 para la resistencia al levantamiento
   
    # resistencianominal_punta_pilote: Resistencia nominal por punta del pilote, Estudio de suelos, kN
    # resistencianominal_friccion_pilote: Resistencia nominal por fricción del pilote, Estudio de suelos, kN
    # 
    # resistencia_mayorada_pilote_resistencia: resistencia mayorada del pilote para el estado límite de resistencia, Art 10.8.3.5-1, kN 
    # resistencia_mayorada_pilote_servicio: resistencia mayorada del pilote para el estado límite de servicio, Art 10.8.3.5-1, kN    
    # resistencia_mayorada_pilote_eventoextremo: resistencia mayorada del pilote para el estado límite de eventoextremo, Art 10.8.3.5-1, kN
    # resistencia_mayorada_pilote_levantamiento: resistencia mayorada del pilote para la resistencia al levantamineto de los pilotes, Art 10.8.3.5-1, kN
    # 
       
    factorderesistencia_punta_resistencia = params['factorderesistencia_punta_resistencia'] = params.get('factorderesistencia_punta_resistencia', 0.5)
    factorderesistencia_friccion_resistencia = params['factorderesistencia_friccion_resistencia'] = params.get('factorderesistencia_friccion_resistencia', 0.55)

    factorderesistencia_punta_servicio = params['factorderesistencia_punta_servicio'] = params.get('factorderesistencia_punta_servicio', 1)
    factorderesistencia_friccion_servicio = params['factorderesistencia_friccion_servicio'] = params.get('factorderesistencia_friccion_servicio', 1)

    factorderesistencia_punta_eventoextremo = params['factorderesistencia_punta_eventoextremo'] = params.get('factorderesistencia_punta_eventoextremo', 1)
    factorderesistencia_friccion_eventoextremo = params['factorderesistencia_friccion_eventoextremo'] = params.get('factorderesistencia_friccion_eventoextremo', 1)

    factorderesistencia_friccion_levantamiento = params['factorderesistencia_friccion_levantamiento'] = params.get('factorderesistencia_friccion_levantamiento', 0.8)

    resistencianominal_punta_pilote = params['resistencianominal_punta_pilote'] = params.get('resistencianominal_punta_pilote', 3433.5)
    resistencianominal_friccion_pilote = params['resistencianominal_friccion_pilote'] = params.get('resistencianominal_friccion_pilote', 2354.4)
    
    resistencia_mayorada_pilote_resistencia = params['resistencia_mayorada_pilote_resistencia'] = factorderesistencia_punta_resistencia * resistencianominal_punta_pilote + factorderesistencia_friccion_resistencia * resistencianominal_friccion_pilote
    resistencia_mayorada_pilote_servicio = params['resistencia_mayorada_pilote_servicio'] = factorderesistencia_punta_servicio * resistencianominal_punta_pilote + factorderesistencia_friccion_servicio * resistencianominal_friccion_pilote
    resistencia_mayorada_pilote_eventoextremo = params['resistencia_mayorada_pilote_eventoextremo'] = factorderesistencia_punta_eventoextremo * resistencianominal_punta_pilote + factorderesistencia_friccion_eventoextremo * resistencianominal_friccion_pilote
    resistencia_mayorada_pilote_levantamiento = params['resistencia_mayorada_pilote_levantamiento'] = - factorderesistencia_friccion_levantamiento * resistencianominal_friccion_pilote
    

    ## Clasificación sismica del puente
    # municipio: Municipio donde se localiza el proyecto
    # departamento: Departamento al cual pertenece el municipio
    # PGA: coeficiente de acelearación pico del terreno, Figura 3.10.2.1-1
    # S1: coeficiente de eaceleración espesctral horizontal, periodo 1s, Figura 3.10.2.1-3
    # clasificacionoperacional: Clasificación operacional, Art. 3.10.5
    # factordesitio: Factor de sitio,  Tabla 3.10.3.2-3
    #
    # zonadedesempeño sísmico: Zona de desempeño sísmico, Tabla 3.10.6-1

    municipio = params['municipio'] = 'Cali'
    
    departamento = params['departamento'] = 'Valle del Cauca'

    PGA = params['PGA'] =params.get('PGA', 0.3)

    S1 = params['S1'] = params.get('S1', 0.3)

    clasificacionoperacional = params['clasificacionoperacional'] = 'Puente esencial'

    factordesitio = params['factordesitio'] = params.get('factordesitio', 1.5)

    SD1 = params['SD1'] = round(factordesitio * S1, 2)

    if SD1 < 0.15 :
        zonadedesempeñosismico = 'Zona 1'
    elif SD1 > 0.15 and SD1 < 0.3 :
        zonadedesempeñosismico = 'Zona 2'
    elif SD1 > 0.3 and SD1 < 0.5 :
       zonadedesempeñosismico = 'Zona 3'
    else :
        zonadedesempeñosismico = 'Zona 4'
    
    params['zonadedesempeñosismico'] = zonadedesempeñosismico

    #Dimensiones del estribo
    # altura_estribo: Altura del estribo, m
    # ancho_estribo: Ancho del estribo, m
    # largo_estribo: Largo del estribo, m
    # altura_vastago: Altura del vástago, m
    # espesor_vástago: Espesor del vástago, m
    # altura_base: Altura de la base del estribo, m
    # ancho_base: Ancho de la base del estribo, m
    # altura_talon: Altura del talón, m
    # ancho_talon: Ancho del talón, m
    # altura_espaldar: Altura del espaldar, m
    # espesor_espaldar: Espesor del espaldar, m
    # distanciaalabase_espaldar: distancia desde el espaldar a la base del estribo, m
    # base_mayor_mensula: base mayor del trapecio de la mensula, m
    # base_menor_mensula: base menor del trapecio de la mensula, m
    # altura_mensula: altura del trapecio de la mensula, m
    # distanciaalabase_mensula: distancia desde la parte inferior de la mensula a la base, m
    # cantidad_topes: Cantidad de topes sísmicos, m
    # altura_topes: Altura de los topes sísmicos, m
    # largo_topes: Largo de los topes sísmicos, m
    # ancho_topes: Ancho de los topes sísmicos, m
    # cantidad_aletas: Cantidad de las aletas, m
    # altura_aletas: Altura de las aletas, m
    # espesor_base_aletas: Espesor de la base de las aletas, m
    # espesor_corona_aletas: Espesor de la corono de las aletas, m
    # altura_losa_aproximacion: altura de la losa de aproximación, m    

    #Estribo
    #  
    altura_estribo = params['altura_estribo'] = params.get('altura_estribo', 8.35) 

    ancho_estribo = params['ancho_estribo'] = params.get('ancho_estribo', 4.4)

    largo_estribo = params['largo_estribo'] = params.get('largo_estribo', 15.9) 

    #Vastago
    altura_vastago = params['altura_vastago'] = params.get('altura_vastago', 4.3)
    espesor_vastago = params['espesor_vastago'] = params.get('espesor_vastago', 1.4)

    #Base
    altura_base = params['altura_base'] = params.get('altura_base', 1.1)
    ancho_base = params['ancho_base'] = params.get('ancho_base', 2.6)

    #Talon
    altura_talon = params['altura_talon'] = params.get('altura_talon', 1.1)
    ancho_talon = params['ancho_talon'] = params.get('ancho_talon', 1.8)

    #Espaldar
    altura_espaldar = params['altura_espaldar'] = params.get('altura_espaldar', 2.8)
    espesor_espaldar = params['espesor_espaldar'] = params.get('espesor_espaldar', 0.45)
    distanciaalabase_espaldar = params['distanciaalabase_espaldar'] = params.get('distanciaalabase_espaldar', 4.35)
   
    # Mensula
    base_mayor_mensula = params['base_mayor_mensula'] = params.get('base_mayor_mensula', 0.5)
    base_menor_mensula = params['base_menor_mensula'] = params.get('base_menor_mensula', 0.3)
    altura_mensula = params['altura_mensula'] = params.get('altura_mensula', 0.15)
    distanciaalabase_mensula = params['distanciaalabase_mensula'] = params.get('distanciaalabase_mensula', 5.5)
   
    #Topes sismicos
    cantidad_topes = params['cantidad_topes'] = params.get('cantidad_topes', 2)
    altura_topes = params['altura_topes'] = params.get('altura_topes', 1.7) 
    largo_topes = params['largo_topes'] = params.get('largo_topes', 0.95)
    ancho_topes = params['ancho_topes'] = params.get('ancho_topes', 1.6)

    #Aletas

    cantidad_aletas = params['cantidad_aletas'] =params.get('cantidad_aletas', 2)
    altura_aletas = params['altura_aletas'] = params.get('altura_aletas', 7.1)
    ancho_aletas = params['ancho_aletas'] = params.get('ancho_aletas', 1.8)
    espesor_base_aletas = params['espesor_base_aletas'] = params.get('espesor_base_aletas', 0.7)
    espesor_corona_aletas = params['espesor_corona_aletas'] = params.get('espesor_corona_aletas', 0.35)

    #losa_aproximacion
    altura_losa_aproximacion = params['altura_losa_aproximacion'] = params.get('altura_losa_aproximacion', 0.3)

    ##Superestructura
    # peso_losa: peso de la losa por m de largo, kN/m
    # L_superestructura:  Longitud de la superestructura, m
    # cantidad_vigas: Cantidad de vigas
    # peso_vigas: peso de las vigas por m de largo, kN/m
    # peso_anden: peso del área transversal del anden por m de largo, kN/m
    # peso_bordillo:peso del bordillo por m de largo, kN/m
    # peso_barandas: peso de las barandas del puente, kN/m
    # numero_diafragmas: cantidad de diafragmas en el puente
    # peso_diafragmas: peso de un diafragma del puente, kN/m
    # ancho_carpetaasfaltica: Ancho de la carpeta asfáltica, m
    # espesor_carpetaasfaltica: Espesor de la carpeta asfáltica, m
    # 
    # Losa
    peso_losa = params['peso_losa'] = params.get('peso_losa', 74.86)

    L_superestructura = params['L_superestructura'] = params.get('L_superestructura', 41)

    #Vigas
    cantidad_vigas = params['cantidad_vigas'] = params.get('cantidad_vigas', 5)
    peso_vigas = params['peso_vigas'] = params.get('peso_vigas', 17.9)

    #Anden
    peso_anden = params['peso_anden'] = params.get('peso_anden', 0)

    #Bordillo
    peso_bordillo = params['peso_bordillo'] = params.get('peso_bordillo', 0 )
   
    #Barandas
    peso_barandas = params['peso_barandas'] = params.get('peso_barandas', 9.2214) 

    #Diafragmas
    numero_diafragmas = params['numero_diafragmas'] = params.get('numero_diafragmas', 2)
    peso_diafragmas = params['peso_diafragmas'] = params.get('peso_diafragma', 109.267)

    #Carpeta asfaltica
    ancho_carpetaasfaltica = params['ancho_carpetaasfaltica'] = params.get('ancho_carpetaasfaltica', 14.4) 

    espesor_carpetaasfaltica = params['espesor_carpetaasfaltica'] = params.get('espesor_carpetaasfaltica', 0.1) 

    #Cargas y momentos provenientes de la superestructura
    # DC_losa: Carga permanente debido al peso propio de la losa sobre el estribo, kN
    # DC_vigas; Carga permanente debido al peso propio de las vigas sobre el estribo, kN
    # DC_sobreimpuestas: Cargas sobre el estribo debido al peso del bordillo, anden, y barandas, kN
    # DC_diafragmas: CArga debido al peso de los diafragmas del puente, kN
    # DW: Carga sobre el estribo debido al peso de la carpeta asfáltica, kN
    #
    # DW_m: Carga sobre el estribo debido al peso de la carpeta asfáltica por m de ancho de estribo, kN
    # DC_total_supestructura: Cargas permanentes provenientes de la superestructura, kN
    # DC_total_superestructura_m:  Cargas permanentes provenientes de la superestructura por m de ancho de estribo, kN
    # X_a: Distancia de aplicación de DC_total_superestructura_m con respecto al punto A, m
    # M_a_DC: Momento de estabilización con respecto al punto A debido a DC_total_superestructura_m, kNm/m
    # M_a_DW: Momento de estabilización con respecto al punto A debido a DW_m, kNm/m


    DC_losa = params['DC_losa'] = round(peso_losa * L_superestructura/2, 2)

    DC_vigas = params['DC_vigas'] = round(cantidad_vigas * peso_vigas* L_superestructura/2, 2)

    DC_diafragmas = params['DC_diafragmas'] = numero_diafragmas * peso_diafragmas 

    DC_sobreimpuestas = params['DC_sobreimpuestas'] = round((peso_anden + peso_bordillo) * L_superestructura/2 + peso_barandas * L_superestructura/2, 2)

    DW = params['DW'] = round(ancho_carpetaasfaltica * espesor_carpetaasfaltica * pesoespecifico_carpetaasfaltica * L_superestructura/2, 2)
    
    DW_m = params['DW_m']= round(DW / largo_estribo, 2)

    #Resumen de cargas y momentos provenientes de superestructura por ancho
    #Momento de estabilizacion debido a las cargas permanentes provenientes de la superestructura
    DC_total_superestructura = params['DC_total_superestructura'] = DC_losa + DC_sobreimpuestas + DC_vigas + DC_diafragmas
    DC_total_superestructura_m = params['DC_total_superestructura_m'] = round(DC_total_superestructura / largo_estribo, 2)
    
    X_a = params['X_a'] = round(ancho_base - espesor_vastago + (largo_topes/2 ), 3)
    M_a_DC = params['M_a_DC'] = round(DC_total_superestructura * X_a, 2) 
    M_a_DW = params['M_a_DW'] = round(DW * X_a, 2 )

    #Cargas provenientes de la superestructura debidas a la carga vehicular de diseño
    # carga_primereje_camion: Carga sobre el primer eje del camión de diseño CCP-14, kN
    # carga_segundoeje_camion: Carga sobre el segundo eje del camión de diseño CCP-14, kN
    # carga_tercereje_camion: Carga sobre el tercer eje del camión de diseño CCP-14, kN
    # carga_total_camion: Carga total del camión de diseño CCP 14, kN
    # distancia_ejes1y2_camión: Distancia entre el primer eje y el segundo eje del camión, m
    # distancia_ejes2y3_camión: Distancia entre el segundo eje y el tercer eje del camión, m
    # carga_primereje_tandem: Carga sobre el primer eje del tándem de diseño CCP-14, kN
    # carga_segundoeje_tandem: Carga sobre el segundo eje del tándem de diseño CCP-14, kN
    # distancia_ejes1y2_tandem: Distancia entre el primer eje y el segundo eje del tándem, m
    # carga_total_tándem: Carga total del tándem de diseño CCP 14, kN
    # carga_carrildiseño: Carga debida al carril de diseño CCP-14, kN/m

    # carga_camion_estribo: Carga producida por el camión de diseño sobre el estribo, kN
    # carga_tandem_estribo: Carga producida por el tándem de diseño sobre el estribo, kN
    # carga_carrildiseño_estribo: Carga producida por el carril de diseño sobre el estribo, kN
    # factor_cargadinamica: Factor de carga dinámica 
    # factor_presencia_multiple: Factor de presencia multiple para dos carriles cargados
    # carga_vehicular_uncarril: Carga sobre el estribo debida a la carga vehicular de diseño CCP-14 para un carril cargado, kN
    # carga_vehicular_numcarriles: Carga sobre el estribo debida a la carga vehicular de diseño CCP-14 para el numero de carriles cargados, kN
    # carga_vehicular_por_m_ancho_estribo: Carga por m de ancho de estribo debido a la carga vehicular de diseño CCP-14, kN/m
    # M_a_LLIM: Momento de estabilización con respecto al punto A debido a la carga vehicular de diseño, kNm/m
     
    # Carga Camión de diseño

    carga_primereje_camion = params['carga_primereje_camion']= 160
    carga_segundoeje_camion = params['carga_segundoeje_camion']= 160
    carga_tercereje_camion = params['carga_tercereje_camion'] = 40
    carga_total_camion = params['carga_total_camion']= carga_primereje_camion + carga_segundoeje_camion + carga_tercereje_camion
    distancia_ejes1y2_camion = params['distancia_ejes1y2_camion'] = 4.3 
    distancia_ejes2y3_camion = params['distancia_ejes2y3_camion'] = 4.3

    #Tandem de diseño
    carga_primereje_tandem = params['carga_primereje_tandem']= 125 
    carga_segundoeje_tandem = params['carga_segundoeje_tandem']= 125
    distancia_ejes1y2_tandem = params['distancia_ejes1y2_camion'] = 1.2
    cargatotal_tandem = params['cargatotal_tandem']= carga_primereje_tandem + carga_segundoeje_tandem

    #Carril de diseño
    carga_carrildiseño = params['carga_carrildiseño'] = 10.3

    carga_camion_estribo = params['carga_camión_estribo']= carga_primereje_camion * 1 + carga_segundoeje_camion * (1 - distancia_ejes1y2_camion / L_superestructura) + carga_tercereje_camion * (1 - (distancia_ejes1y2_camion + distancia_ejes2y3_camion)/L_superestructura )
    carga_tandem_estribo = params['carga_tandem_estribo']= carga_primereje_tandem * 1 + carga_segundoeje_tandem * (1 - distancia_ejes1y2_tandem / L_superestructura)
    carga_carrildiseño_estribo = params['carga_carrildiseño_estribo'] = carga_carrildiseño * L_superestructura / 2 * 1

    #Carga sobre el estribo dibido a la carga vehicular de diseño
    factor_cargadinamica = params['factor_cargadinamica'] = 1.33

    factor_presenciamultiple = params['factor_presenciamultiple'] = 0.65

    if carga_camion_estribo > carga_tandem_estribo :
        carga_vehicular_uncarril = round(factor_presenciamultiple*(factor_cargadinamica * carga_camion_estribo + carga_carrildiseño_estribo), 2)
    else :
        carga_vehicular_uncarril = round(factor_presenciamultiple*(factor_cargadinamica * carga_tandem_estribo + carga_carrildiseño_estribo), 2)

    params['carga_vehicular_uncarril'] = carga_vehicular_uncarril 

    carga_vehicular_numcarriles = params['carga_vehicular_numcarriles'] = round(numero_carriles * carga_vehicular_uncarril, 2) 

    carga_vehicular_por_m_ancho_estribo = params['carga_vehicular_por_m_ancho_estribo'] = round(carga_vehicular_numcarriles / largo_estribo, 2)
    #Momento de estabilización con respecto al punto A debido a la carga vehicular de diseño
    M_a_LLIM = params['M_a_LLIM'] = round(carga_vehicular_numcarriles * X_a, 2)

    #Fuerza de Frenado
    # BR_25: 25% del peso de los ejes del camión o tándem de diseño, kN
    # BR_5: 5% del camión o tándem de diseño más la carga de carril, kN
    # BR_e: Fuerza de frenado por m de ancho de estribo, kN/m
    # M_a_BR: Momento de desestabilización con respecto al punto A debido a la fuerza de frenado, kNm/m
     
    BR_25 = params['BR_25'] = numero_carriles * factor_presenciamultiple * 0.25 * carga_total_camion
    BR_5 = params['BR_5'] = 0.05 *numero_carriles * factor_presenciamultiple * (carga_total_camion + carga_carrildiseño * L_superestructura) 
    if BR_25 > BR_5 :
        BR_e = BR_25 
    else :
        BR_e = BR_5 

    params['BR_e'] = BR_e
    M_a_BR = params['M_a_BR'] = BR_e * (altura_estribo + 1.8 )

    #Cargas y momentos debidos al peso de la subestructura
    # DC_'parte de estribo': Peso del concreto de la 'parte de estribo' por m de ancho de estribo, kN/m
    # X_a_'parte de estribo': Distancia en el eje x desde el punto A hasta el centro de gravedad de la 'parte de estribo', m 
    # Y_a_'parte de estribo': Distancia en el eje y desde el punto A hasta el centro de gravedad de la 'parte de estribo', m
    # DC_X_a_'parte de estribo': Momento generado por peso de la 'parte de estribo' sobre el Punto A, kNm/m
    # DC_Y_a_'parte de estribo': Momento generado por peso de la 'parte de estribo' sobre el Punto A, kNm/m
    # DC_losa_aproximacion: Peso de la losa de aproximación, kN

    

    #Peso del estribo
    DC_zapata = pesoespecifico_concreto *(ancho_base + ancho_talon) * ((altura_base + altura_talon) / 2)* largo_estribo
    X_a_zapata = (ancho_base +ancho_talon) / 2
    Y_a_zapata = ((altura_base + altura_talon) / 2) / 2
    DC_X_a_zapata = DC_zapata * X_a_zapata
    DC_Y_a_zapata = DC_zapata * Y_a_zapata
    params['DC_zapata'] = round(DC_zapata, 2)
    params['X_a_zapata'] = round(X_a_zapata, 3)
    params['Y_a_zapata'] = round(Y_a_zapata, 3)
    params['DC_X_a_zapata'] = round(DC_X_a_zapata, 2)
    params['DC_Y_a_zapata'] = round(DC_Y_a_zapata,2)

    DC_vastago = pesoespecifico_concreto * (espesor_vastago * altura_vastago)* largo_estribo
    X_a_vastago = ancho_base - espesor_vastago / 2
    Y_a_vastago = ((altura_base + altura_talon) / 2) + altura_vastago /2
    DC_X_a_vastago = DC_vastago * X_a_vastago
    DC_Y_a_vastago = DC_vastago * Y_a_vastago

    params['DC_vastago'] = round(DC_vastago, 2)
    params['X_a_vastago'] = round(X_a_vastago, 3)
    params['Y_a_vastago'] = round(Y_a_vastago, 3)
    params['DC_X_a_vastago'] = round(DC_X_a_vastago, 2)
    params['DC_Y_a_vastago'] = round(DC_Y_a_vastago, 2)

    DC_espaldar = pesoespecifico_concreto * espesor_espaldar * altura_espaldar * largo_estribo
    X_a_espaldar = ancho_base - espesor_espaldar / 2
    Y_a_espaldar = ((altura_base + altura_talon) / 2) + distanciaalabase_espaldar +altura_espaldar / 2 
    DC_X_a_espaldar = DC_espaldar * X_a_espaldar
    DC_Y_a_espaldar = DC_espaldar * Y_a_espaldar

    params['DC_espaldar'] = round(DC_espaldar, 2)
    params['X_a_espaldar'] = round(X_a_espaldar, 3)
    params['Y_a_espaldar'] = round(Y_a_espaldar, 3)
    params['DC_X_a_espaldar'] = round(DC_X_a_espaldar, 2)
    params['DC_Y_a_espaldar'] = round(DC_Y_a_espaldar, 2)

    DC_mensula = pesoespecifico_concreto *(base_mayor_mensula+base_menor_mensula)/2*altura_mensula * largo_estribo
    X_a_mensula = ancho_base + altura_mensula/2
    Y_a_mensula = ((altura_base + altura_talon) / 2) + distanciaalabase_mensula +base_mayor_mensula / 2 
    DC_X_a_mensula = DC_mensula * X_a_mensula
    DC_Y_a_mensula = DC_mensula * Y_a_mensula

    params['DC_mensula'] = round(DC_mensula, 2)
    params['X_a_mensula'] = round(X_a_mensula, 3)
    params['Y_a_mensula'] = round(Y_a_mensula, 3)
    params['DC_X_a_mensula'] = round(DC_X_a_mensula, 2)
    params['DC_Y_a_mensula'] = round(DC_Y_a_mensula, 2)


    DC_topes = (pesoespecifico_concreto * cantidad_topes * altura_topes * ancho_topes * largo_topes )
    X_a_topes = ancho_base - espesor_espaldar-ancho_topes / 2
    Y_a_topes = ((altura_base + altura_talon) / 2) + altura_vastago + altura_topes / 2
    DC_X_a_topes = DC_topes * X_a_topes
    DC_Y_a_topes = DC_topes * Y_a_topes

    params['DC_topes'] = round(DC_topes, 2)
    params['X_a_topes'] = round(X_a_topes, 3)
    params['Y_a_topes'] = round(Y_a_topes, 3)
    params['DC_X_a_topes'] = round(DC_X_a_topes, 2)
    params['DC_Y_a_topes'] = round(DC_Y_a_topes, 2)

    DC_aletas = pesoespecifico_concreto * cantidad_aletas * (altura_aletas * ancho_aletas - espesor_espaldar * altura_espaldar) * ((espesor_base_aletas + espesor_corona_aletas )/2) 
    X_a_aletas = (ancho_estribo -(ancho_talon)/2)
    Y_a_aletas = ((altura_aletas * espesor_corona_aletas * (altura_aletas /2 + altura_base)) + (0.5 * altura_aletas * (espesor_base_aletas - espesor_corona_aletas ) * (altura_aletas/3 + altura_base))) / ((altura_aletas * espesor_corona_aletas) + 0.5 * altura_aletas *(espesor_base_aletas - espesor_corona_aletas))
    DC_X_a_aletas = DC_aletas * X_a_aletas
    DC_Y_a_aletas = DC_aletas * Y_a_aletas

    params['DC_aletas'] = round(DC_aletas, 2)
    params['X_a_aletas'] = round(X_a_aletas, 3)
    params['Y_a_aletas'] = round(Y_a_aletas, 3)
    params['DC_X_a_aletas'] = round(DC_X_a_aletas, 2)
    params['DC_Y_a_aletas'] = round(DC_Y_a_aletas, 2)

    DC_losa_aproximacion = params['DC_losa_aproximacion'] = params.get('DC_losa_aproximacion',245.25)
    X_a_losa_aproximacion = ancho_base  + altura_mensula/2
    Y_a_losa_aproximacion = ((altura_base + altura_talon) / 2) + distanciaalabase_mensula +base_mayor_mensula + altura_losa_aproximacion/2
    DC_X_a_losa_aproximacion = DC_losa_aproximacion * X_a_losa_aproximacion
    DC_Y_a_losa_aproximacion = DC_losa_aproximacion * Y_a_losa_aproximacion

    params['DC_losa_aproximacion'] = round(DC_losa_aproximacion, 2)
    params['X_a_losa_aproximacion'] = round(X_a_losa_aproximacion, 3)
    params['Y_a_losa_aproximacion'] = round(Y_a_losa_aproximacion, 3)
    params['DC_X_a_losa_aproximacion'] = round(DC_X_a_losa_aproximacion, 2)
    params['DC_Y_a_losa_aproximacion'] = round(DC_Y_a_losa_aproximacion, 2)

    DC_total_estribo = DC_zapata + DC_vastago + DC_espaldar + DC_topes + DC_aletas + DC_mensula +DC_losa_aproximacion
    params['DC_total_estribo'] = round(DC_total_estribo, 2)

    suma_DC_X_a = DC_X_a_zapata + DC_X_a_vastago + DC_X_a_espaldar + DC_X_a_topes + DC_X_a_aletas 
    params['suma_DC_X_a'] = round(suma_DC_X_a, 2)

    suma_DC_Y_a = DC_Y_a_zapata + DC_Y_a_vastago + DC_Y_a_espaldar + DC_Y_a_topes + DC_Y_a_aletas
    params['suma_DC_Y_a'] = round(suma_DC_Y_a, 2)
   
    X_a_estribo = round(suma_DC_X_a / DC_total_estribo, 2)
    params['X_a_estribo'] = X_a_estribo
    
    Y_a_estribo = round(suma_DC_Y_a / DC_total_estribo, 2)
    params['Y_a_estribo'] = Y_a_estribo

    #Carga y momentos debidos al peso propio del relleno
    # DC_relleno: Peso del relleno por m de ancho de estribo, kN/m
    # X_a_relleno: Distancia en el eje x desde el punto A hasta el centro de gravedad de la 'parte de estribo', m 
    # Y_a_relleno: Distancia en el eje y desde el punto A hasta el centro de gravedad de la 'parte de estribo', m
    # DC_X_a_relleno: Momento generado por peso del relleno sobre el punto A, kNm/m
    # DC_Y_a_relleno: Momento generado por peso del relleno sobre el punto A, kNm/m

    DC_relleno = pesoespecifico_suelo * (altura_aletas * ancho_aletas ) * ((largo_estribo - 2 * espesor_base_aletas) + (espesor_base_aletas-espesor_corona_aletas))
    params['DC_relleno'] = round(DC_relleno, 2)
    
    X_a_relleno = (ancho_estribo - (ancho_talon) / 2)
    params['X_a_relleno'] = round(X_a_relleno, 2)

    Y_a_relleno = (altura_base + altura_talon) / 2 + altura_aletas / 2
    params['Y_a_relleno'] = round(Y_a_relleno, 2 )

    DC_X_a_relleno = DC_relleno * X_a_relleno
    params['DC_X_a_relleno'] = round(DC_X_a_relleno, 2)

    DC_Y_a_relleno = DC_relleno * Y_a_relleno
    params['DC_Y_a_relleno'] = round(DC_Y_a_relleno, 2)    

    #Sobrecarga LS por carga viva sobre el relleno
    # tetha_ka: Ángulo de la cara trasera del muro con respecto a la horizontal como se muestra en la figura 3.11.5.3-1, Grados
    # beta_ka: Angulo del relleno con respecto a la  horizontal como se muestra en la figura 3.11.5.3.-1., Grados

    # coeficiente_presion_lateral_activa_suelo: coeficiente de presión lateral del suelo [Ka]
    # coeficiente_presion_lateral_activa_suelo_desf: coeficiente de presión lateral del suelo para la condición más desfavorable [Ka]    
    # altura_equivalente_suelo: altura equivalente de suelo para carga vehicular, m, Tabla 3.11.6.4.1
    # presion_horizontal_suelo_sobrecargaviva: presión constante horizontal de suelo debida a la sobrecarga por carga viva, Art 3.11.6.4, MPa , Nota: la ecuación descrita en la norma la cual incluye un factor de 10**-9 no tiene sentido físico, por ello no se usa ese factor.
    # L_S_x = componente horizontal de la  presión constante horizontal de suelo debida a la sobrecarga por carga viva por m de ancho de estribo, kN/m
    # M_a_LS_x: Momento de desestabilización en el punto A debido a la sobrecarga por carga viva por m de ancho de estribo, kNm/m
    # L_S_y: componente vertical de la presión constante horizontal de suelo debida a la sobrecarga por carga viva por m de ancho de estribo, kN/m
    # Y_a_LS: longitud cargada con la sobrecarga por carga viva, m
    # M_a_LS_y: Momento de estabilización en el punto A debido a la sobrecarga por carga viva por m de ancho de estribo, kNm/m
    tetha_ka = params['tetha_ka'] = params.get('tetha_ka', 90)
    beta_ka = params['beta_ka'] = params.get('beta_ka', 0)
    coeficiente_presion_lateral_activa_suelo = params['coeficiente_presion_lateral_activa_suelo'] = (math.sin(math.radians(tetha_ka + angulodefriccioninternadelsuelorelleno)))** 2/((math.sin(math.radians(tetha_ka))**2 * math.sin(math.radians(tetha_ka-angulodefricciondelsueloconcreto))* (1+((math.sin(math.radians(angulodefriccioninternadelsuelorelleno+angulodefricciondelsueloconcreto)))*(math.sin(math.radians(angulodefriccioninternadelsuelorelleno-beta_ka)))/((math.sin(math.radians(tetha_ka-angulodefricciondelsueloconcreto)))*(math.sin(math.radians(tetha_ka + beta_ka)))))**0.5)**2)) 
    
    coeficiente_presion_lateral_activa_suelo_desf = params['coeficiente_presion_lateral_activa_suelo_desf'] = (math.sin(math.radians(tetha_ka + angulodefriccioninternadelsuelorelleno)))** 2/((math.sin(math.radians(tetha_ka))**2 * math.sin(math.radians(tetha_ka))* (1+((math.sin(math.radians(angulodefriccioninternadelsuelorelleno)))*(math.sin(math.radians(angulodefriccioninternadelsuelorelleno-beta_ka)))/((math.sin(math.radians(tetha_ka)))*(math.sin(math.radians(tetha_ka + beta_ka)))))**0.5)**2)) 
    
    if altura_estribo <= 3  : 
        altura_equivalente_suelo = -0.2 * altura_estribo + 1.5
    elif altura_estribo < 6 and altura_estribo > 3 :
        altura_equivalente_suelo = -0.1 * altura_estribo + 1.2
    else :
        altura_equivalente_suelo = 0.6
    presion_horizontal_suelo_sobrecargaviva = params['presion_horizontal_suelo_sobrecargaviva'] = round(coeficiente_presion_lateral_activa_suelo_desf * pesoespecifico_suelo * altura_equivalente_suelo, 2) 
    
    params['altura_equivalente_suelo'] = altura_equivalente_suelo

    # componente horizontal y momento de desestabilización en A para la altura total del estribo

    L_S_x = params['L_S_x'] = round(presion_horizontal_suelo_sobrecargaviva * altura_estribo * largo_estribo, 2) 
    M_a_LS_x = params['M_a_LS_x'] = round(L_S_x * altura_estribo / 2, 2)

    # Componente vertical y momento de estabilización con respecto al punto A para longitud cargada 
    L_S_y = params['L_S_y'] = round(presion_horizontal_suelo_sobrecargaviva * (ancho_talon)* largo_estribo, 2)
    Y_a_LS = params['Y_a_LS'] = round((ancho_estribo - (ancho_talon) / 2), 2)
    M_a_LS_y = params['M_a_LS_y'] = round(L_S_y * Y_a_LS, 2)

    # Acciones verticales por m de estribo
    # suma_cargas_verticales_estribo: cargas verticales totales que actuan sobre el estribo, kN/m
    # suma_M_a_estribo: Momento sobre el punto A debido a las cargas verticales que actuan sobre el estribo, kNm/m 

    suma_cargas_verticales_estribo = params['suma_cargas_verticales_estribo'] = round(DC_total_superestructura +DC_total_estribo + DW_m +DC_relleno +carga_vehicular_numcarriles + L_S_y, 2)
    suma_M_a_estribo = params['suma_M_a_estribo'] = round(suma_DC_X_a + M_a_DC +M_a_DW + DC_X_a_relleno + M_a_LLIM + M_a_LS_y, 2)
    
    ## Empuje horizontal del suelo 
    # coeficiente_presion_activa_suelo: coeficiente de presión activa del suelo [Ka]
    # empuje_activo_estatico_EH: empuje activo estático, kN/m
    # Y_a_EH: distancia desde el punto A a la linea de acción de la fuerza resultante del empuje activo, m
    # M_a_EH: Momento de desestabilización producido por el empuje activo EH del terreno, kNm/m
     
    #coeficiente_presion_activa_suelo = params['coeficiente_presion_activa_suelo'] = round((1-math.sin(angulodefriccioninternadelsuelodecimentacion/180*math.pi)) / (1+math.sin(angulodefriccioninternadelsuelodecimentacion/180*math.pi)),3)
    empuje_activo_estatico_EH = params['empuje_activo_estatico_EH'] = round(pesoespecifico_suelo * coeficiente_presion_lateral_activa_suelo_desf * altura_estribo ** 2 * largo_estribo/ 2, 2)
    Y_a_EH = params['Y_a_EH'] = round(altura_estribo / 3, 2)
    M_a_EH = params['M_a_EH'] = round(empuje_activo_estatico_EH * Y_a_EH, 2)
    
    ## Fuerzas sismicas
    # F_PGA: factor de sitio en el periodo de vibración cero del espectro de aceleraciones, Tabla 3.10.3.2-1
    # k_h0: Coeficiente sísmico de aceleración horizontal, (suposición que el estribo no se desplaza), Art. 11.6.5.2.1
    # k_h: Coeficiente sísmico de aceleración horizontal, Art. 11.6.5.2.2
    # kv: Coeficiente sísmico de aceleración vertical, Art 11.6.5.2.2
    # beta_estribo: ángulo beta utilizado en el método Mononobe Okabe, Grados, Figura A11.3.1-1
    # delta_estribo: ángulo delta utilizado en el método Mononobe Okabe, Grados, Figura A11.3.1-1
    # i_estribo: ángulo i utilizado en el método Mononobe Okabe, Grados, Figura A11.3.1-1 
    # theta_Mo: ángulo theta_Mo utlizado en el método Mononobe Okabe, Grados, Art A11.3.1-1
    # K_AE: coeficiente de presión sísmica activa del suelo, Art A11.3.1-1
    # P_AE: Fuerza sísmica debida al empuje del terreno por m de estribo, kN/m , Art 11.6.5.3-2
    # delta_P_AE: Diferencia entre el empuje activo estático y el empju del terreno debido al sismo, kN/m
    # distancia_aplicacion_deltaP_AE: distancia de aplicación de delta_P_AE, m, Art A11.3.1
    # M_a_delta_P_AE = Momento producido por delta_P_AE sobre el punto A, kNm/m
    # 
    F_PGA = params['F_PGA'] = params.get('F_PGA',1.1)
    k_h0 = params['k_h0'] = F_PGA * PGA
    k_h = params['k_h'] = 0.5 * k_h0

    kv = params['kv'] = params.get('kv',0)
    beta_estribo = params['beta_estribo'] = params.get('beta_estribo',0)
    delta_estribo = params['delta_estribo'] = params.get('delta_estribo', 0)
    i_estribo = params['i_estribo'] = params.get('i_estribo',0)
   
    theta_Mo = params['theta_Mo'] = round(math.atan(k_h/(1-kv)) *180 / math.pi, 2)
    
    K_AE = params['K_AE']= round((math.cos((angulodefriccioninternadelsuelorelleno-theta_Mo-beta_estribo)* math.pi /180 )) ** 2 / ((math.cos(theta_Mo /180 * math.pi)) * (math.cos(beta_estribo * math.pi/ 180)) **2 * math.cos((delta_estribo + beta_estribo +theta_Mo)/180* math.pi)) * (1+ math.sqrt((math.sin((angulodefriccioninternadelsuelorelleno + delta_estribo)/180*math.pi)*math.sin((angulodefriccioninternadelsuelorelleno - theta_Mo - i_estribo)/180* math.pi))/(math.cos((delta_estribo +beta_estribo + theta_Mo)/180*math.pi)*math.cos((i_estribo - beta_estribo)/180*math.pi))))**-2, 3)
    P_AE = params['P_AE'] = round(0.5 * K_AE * pesoespecifico_suelo * altura_estribo ** 2 * largo_estribo, 2)
    delta_P_AE = params['delta_P_AE'] = round(P_AE - empuje_activo_estatico_EH, 2)
    distancia_aplicacion_deltaP_AE = params['distancia_aplicacion_deltaP_AE'] = round(0.4 * altura_estribo, 2)
    M_a_delta_P_AE = params['M_a_delta_P_AE'] = round(delta_P_AE * distancia_aplicacion_deltaP_AE, 2)

    # Calculo de fuerza PIR
    # P_IR: Fuerza horizontal debida a la fuerza sísmica de la masa del muro, kN/m, Art 11.6.5.1-1
    P_IR = params['P_IR'] = round(k_h *( DC_relleno + DC_total_estribo), 2)

    # Combinacion mas desfavorble de fuerzas debidas al sismo
    # Pseis_1: combinación: 100% del empuje activo sísmico + 50% de la fuerza sísmica debida al peso del suelo de relleno, kN
    # Pseis_2: combinación: 50% del empuje activo sísmico + 100% de la fuerza sísmica debida al peso del suelo de relleno, kN
    # Pseis_3: combinación: 100% del empuje estático + 50% de la fuerza sísmica debida al peso del suelo de relleno, kN, Nota: Esta combinación no está incluida en la Norma CCP-14)
    
    # Pseis_e: Combinación de mayor valor , kN
    # M_a_P_seis: Momento producido por P_seis sobre el punto A, kNm/m

    Pseis_1 = params['Pseis_1'] = round(delta_P_AE + 0.5 * P_IR, 2)
    Pseis_2 = params['Pseis_2'] = round(0.5* empuje_activo_estatico_EH + P_IR, 2)
    Pseis_3 = params['Pseis_3'] = round(empuje_activo_estatico_EH + 0.5 * P_IR ,2)
    if Pseis_1 > Pseis_2 and Pseis_1> Pseis_3 :
        Pseis_e =  Pseis_1
    elif Pseis_2 > Pseis_1 and Pseis_2> Pseis_3:
        Pseis_e = Pseis_2
    elif Pseis_3 > Pseis_1 and Pseis_3> Pseis_2 :
        Pseis_e = Pseis_3
    M_a_p_seis = params['M_a_p_seis'] = round(distancia_aplicacion_deltaP_AE * Pseis_e, 2)

    params['Pseis_e'] = round(Pseis_e, 2)
    
    #Fuerza sismica Hbu proveniente de la superestructura
    # coeficiente_friccion: Coeficiente de fricción, 0.2 valor promedio empleado para dispositivos elastoméricos apoyados sobre concreto y acero
    #
    # P_u: Fuerza de compresión, obtenida a partir de combinaciones de resistencia y evento extremo, kN/m, Tabla 3.4.1-1
    # Hbu: Carga lateral transmitida a la superestructura y a la infraestructura por los apoyos, kN/m, Art 14.6.3.1-1
    # distancia_aplicacion_Hbu: La fuerza Hbu se aplica a la altura del apoyo de las vigas, m
    # M_a_Hbu: Momento de desestbilización de la fuerza horizontal Hbu, con respecto al punto A, kNm/m
    # suma_fuerzas_sismicas: Sumatoria de fuerzas sísmicas (Pseis y Hbu), kN/m
    # suma_M_a_fuerzas_sismicas: Sumatoria de momentos respecto al punto A debidos a fuerzas sísmicas, kNm/m
    
    coeficiente_friccion = params['coeficiente_friccion'] = params.get('coeficiente_friccion', 0.2)
    P_u = params['P_u'] = round(1.25 * DC_total_superestructura + 1.5 * DW + 0.5 * carga_vehicular_numcarriles,2)
    Hbu =params['Hbu'] = round(coeficiente_friccion * P_u, 2)
    distancia_aplicacion_Hbu = params['distancia_aplicacion_Hbu'] = round(altura_base + altura_vastago, 2)
    M_a_Hbu = params['M_a_Hbu'] = round(distancia_aplicacion_Hbu * Hbu, 2)


    suma_fuerzas_sismicas = params['suma_fuerzas_sismicas'] = round(Pseis_e + Hbu, 2)
    suma_M_a_fuerzas_sismicas = params['suma_M_a_fuerzas_sismicas'] = round(M_a_p_seis + M_a_Hbu, 2)
    
    #Longitud de apoyo

    S_angulo_sesgo = params['S_angulo_sesgo'] = params.get('S_angulo_sesgo',0 )
    altura_columnas = params['altura_columnas'] = params.get('altura_columnas', 0 )
    mayoración_N = params['mayoracion_N'] = params.get('mayoracion_N', 1.5 ) 
    longitud_apoyo = params['longitud_apoyo'] = round(mayoración_N * ((200 + 0.0017 * L_superestructura * 1000 + 0.0067 * altura_columnas * 1000) + (1 + 0.000125 * (S_angulo_sesgo * 1000) ** 2))/1000, 2)
    limite_longitud_apoyo = params['limite_longitud_apoyo'] = round(espesor_vastago - espesor_espaldar,2)
    if longitud_apoyo > limite_longitud_apoyo :
        print('No cumple longitud de apoyo')
    
    #Verificacion por estabilidad al volcamiento y al deslizamiento
    # factor_carga_[ ]_max: Factor de carga máximo para el tipo de carga especificado, Tabla 3.4.1.2 
    # factor_carga_[ ]_min: Factor de carga mínimo para el tipo de carga especificado, Tabla 3.4.1.2
    # fuerza_max_vertical_[]: Combinación máxima de fuerzas para el estado límite especificado, kN/m    
    # fuerza_min_vertical_[]: Combinación mínima de fuerzas para el estado límite especificado, kN/m
    # momento_max_vertical_[]: Combinación máxima de momentos para el estado límite especificado, kNm/m    
    # momento_min_vertical_[]: Combinación mínima de momentos para el estado límite especificado, kNm/m  
    # fuerza_max_horizontal_[]: Combinación máxima de fuerzas para el estado límite especificado, kN/m    
    # fuerza_min_horizontal_[]: Combinación mínima de fuerzas para el estado límite especificado, kN/m
    # momento_max_horizontal_[]: Combinación máxima de momentos para el estado límite especificado, kNm/m    
    # momento_min_horizontal_[]: Combinación mínima de momentos para el estado límite especificado, kNm/m 

    factor_carga_DC_max = params['factor_carga_DC_max'] = params.get('factor_carga_DC_max', 1.25)
    factor_carga_DC_min = params['factor_carga_DC_min'] = params.get('factor_carga_DC_min', 0.9)
    factor_carga_DW_max = params['factor_carga_DW_max'] = params.get('factor_carga_DW_max', 1.5)
    factor_carga_DW_min = params['factor_carga_DW_min'] = params.get('factor_carga_DW_min', 0.65)
    factor_carga_EH_max = params['factor_carga_EH_max'] = params.get('factor_carga_EH_max', 1.5)
    factor_carga_EH_min = params['factor_carga_EH_min'] = params.get('factor_carga_EH_min', 0.9)
    factor_carga_EV_eg_max = params['factor_carga_EV_max'] = params.get('factor_carga_EV_max', 1)
    factor_carga_EV_eg_min = params['factor_carga_EV_min'] = params.get('factor_carga_EV_min', 0)    
    factor_carga_EV_MyE_max = params['factor_carga_EV_MyE_max'] = params.get('factor_carga_EV_MyE_max', 1.35)
    factor_carga_EV_MyE_min = params['factor_carga_EV_MyE_min'] = params.get('factor_carga_EV_MyE_min', 1)
    factor_carga_ES_max = params['factor_carga_ES_max'] = params.get('factor_carga_ES_max', 1.5)
    factor_carga_ES_min = params['factor_carga_ES_min'] = params.get('factor_carga_ES_min', 0.75)
    factor_carga_EQ_max = params['factor_carga_EQ_max'] = params.get('factor_carga_EQ_max', 1)
    factor_carga_EQ_min = params['factor_carga_EQ_min'] = params.get('factor_carga_EQ_min', 1)
    factor_carga_LS_max = params['factor_carga_LS_max'] = params.get('factor_carga_LS_max', 1.75)
    factor_carga_LS_min = params['factor_carga_LS_min'] = params.get('factor_carga_LS_min', 0)
    factor_carga_LS_EE_max = params['factor_carga_LS_EE_max'] = params.get('factor_carga_LS_EE_max', 0.5)
    factor_carga_LS_EE_min = params['factor_carga_LS_EE_min'] = params.get('factor_carga_LS_EE_min', 0)
    
    fuerza_max_vertical_resistencia = params['fuerza_max_vertical_resistencia'] = round(factor_carga_DC_max * DC_total_superestructura + factor_carga_DC_max * DC_total_estribo + factor_carga_DW_max * DW + factor_carga_EV_MyE_max * DC_relleno + factor_carga_LS_max * carga_vehicular_numcarriles + factor_carga_LS_max * L_S_y, 2)
    fuerza_min_vertical_resistencia = params['fuerza_min_vertical_resistencia'] = round(factor_carga_DC_min * DC_total_superestructura + factor_carga_DC_min * DC_total_estribo + factor_carga_DW_min * DW + factor_carga_EV_MyE_min * DC_relleno + factor_carga_LS_min * carga_vehicular_numcarriles + factor_carga_LS_min * L_S_y, 2)
    fuerza_max_vertical_eventoextremo = params['fuerza_max_vertical_eventoextremo'] = round(factor_carga_DC_max * DC_total_superestructura + factor_carga_DC_max * DC_total_estribo + factor_carga_DW_max * DW + factor_carga_EV_MyE_max * DC_relleno + factor_carga_LS_EE_max * carga_vehicular_numcarriles + factor_carga_LS_EE_max * L_S_y, 2)
    fuerza_min_vertical_eventoextremo = params['fuerza_min_vertical_eventoextremo'] = round(factor_carga_DC_min * DC_total_superestructura + factor_carga_DC_min * DC_total_estribo + factor_carga_DW_min * DW + factor_carga_EV_MyE_min * DC_relleno + factor_carga_LS_EE_min * carga_vehicular_numcarriles + factor_carga_LS_EE_min * L_S_y, 2)
    fuerza_vertical_servicio = params['fuerza_vertical_servicio'] = round( DC_total_superestructura +  DC_total_estribo + DW + DC_relleno + carga_vehicular_numcarriles + L_S_y, 2)

    momento_max_vertical_resistencia = params['momento_max_vertical_resistencia'] = round( factor_carga_DC_max * M_a_DC + factor_carga_DC_max * suma_DC_X_a + factor_carga_DW_max * M_a_DW + factor_carga_EV_MyE_max * DC_X_a_relleno + factor_carga_LS_max * M_a_LLIM + factor_carga_LS_max * M_a_LS_y ,2)
    momento_min_vertical_resistencia = params['momento_min_vertical_resistencia'] = round( factor_carga_DC_min * M_a_DC + factor_carga_DC_min * suma_DC_X_a + factor_carga_DW_min * M_a_DW + factor_carga_EV_MyE_min * DC_X_a_relleno + factor_carga_LS_min * M_a_LLIM + factor_carga_LS_min * M_a_LS_y ,2)
    momento_max_vertical_eventoextremo = params['momento_max_vertical_eventoextremo'] = round( factor_carga_DC_max * M_a_DC + factor_carga_DC_max * suma_DC_X_a + factor_carga_DW_max * M_a_DW + factor_carga_EV_MyE_max * DC_X_a_relleno + factor_carga_LS_EE_max * M_a_LLIM + factor_carga_LS_EE_max * M_a_LS_y ,2)
    momento_min_vertical_eventoextremo = params['momento_min_vertical_eventoextremo'] = round( factor_carga_DC_min * M_a_DC + factor_carga_DC_min * suma_DC_X_a + factor_carga_DW_min * M_a_DW + factor_carga_EV_MyE_min * DC_X_a_relleno + factor_carga_LS_EE_min * M_a_LLIM + factor_carga_LS_EE_min * M_a_LS_y ,2)
    momento_vertical_servicio = params['momento_vertical_servicio'] = round( M_a_DC + suma_DC_X_a + M_a_DW + DC_X_a_relleno + M_a_LLIM + M_a_LS_y ,2)

    fuerza_max_horizontal_resistencia = params['fuerza_max_horizontal_resistencia'] = round( factor_carga_EH_max * empuje_activo_estatico_EH + factor_carga_LS_max * (L_S_x + BR_e) , 2)
    fuerza_min_horizontal_resistencia = params['fuerza_min_horizontal_resistencia'] = round( factor_carga_EH_min * empuje_activo_estatico_EH + factor_carga_LS_min * (L_S_x + BR_e) , 2)
    fuerza_max_horizontal_eventoextremo = params['fuerza_max_horizontal_eventoextremo'] = round( factor_carga_EH_max * empuje_activo_estatico_EH + factor_carga_LS_EE_max * (L_S_x + BR_e) + factor_carga_EQ_max * Pseis_e + factor_carga_EQ_max * Hbu, 2)
    fuerza_min_horizontal_eventoextremo = params['fuerza_min_horizontal_eventoextremo'] = round( factor_carga_EH_min * empuje_activo_estatico_EH + factor_carga_LS_EE_min * (L_S_x + BR_e) + factor_carga_EQ_min * Pseis_e + factor_carga_EQ_min * Hbu, 2)
    fuerza_horizontal_servicio = params['fuerza_horizontal_servicio'] = round( empuje_activo_estatico_EH + L_S_x + BR_e, 2)

    momento_max_horizontal_resistencia = params['momento_max_horizontal_resistencia'] = round( factor_carga_EH_max * M_a_EH + factor_carga_LS_max * (M_a_LS_x + M_a_BR) , 2)
    momento_min_horizontal_resistencia = params['momento_min_horizontal_resistencia'] = round( factor_carga_EH_min * M_a_EH + factor_carga_LS_min * (M_a_LS_x + M_a_BR) , 2)
    momento_max_horizontal_eventoextremo = params['momento_max_horizontal_eventoextremo'] = round( factor_carga_EH_max * M_a_EH + factor_carga_LS_EE_max * (M_a_LS_x+M_a_BR) + factor_carga_EQ_max * M_a_p_seis + factor_carga_EQ_max * M_a_Hbu, 2)
    momento_min_horizontal_eventoextremo = params['momento_min_horizontal_eventoextremo'] = round( factor_carga_EH_min * M_a_EH + factor_carga_LS_EE_min * (M_a_LS_x+M_a_BR) + factor_carga_EQ_min * M_a_p_seis + factor_carga_EQ_min * M_a_Hbu, 2)
    momento_horizontal_servicio = params['momento_horizontal_servicio'] = round( M_a_EH + M_a_LS_x + M_a_BR, 2) 
    
    # Cargas Verticales sobre pilotes
    # num_pilotes: Número total de pilotes en el estribo
    # distancia_pilote_cg: Distancia desde el centro del pilote al eje donde se sitúa el centro de gravedad de los pilotes, m
    
    # d_[]_[]: distancia de aplicación de la resultante vertical respecto al punto A para el caso de solicitciones [máximas o  mínimas] en el estado de límite especificado, m
    # e_[]_[]: excentricidad medida desde el centro de la base del estribo para el caso de solicitciones [máximas o mínimas] en el estado de límite especificado, m

    # carga_pilote_eje[]_[]_[]: Carga vertical sobre el pilte en el eje [a o b] para el caso [mínimo o  máximo] del estado límite especificado, kN
    
    
    num_pilotes = params['num_pilotes'] = params.get('num_pilotes', 14)
    distancia_pilote_cg = params['distancia_pilote_cg'] = params.get('distancia_pilote_cg', 1.4)

    d_max_resistencia = params['d_max_resistencia'] = round((momento_max_vertical_resistencia - momento_max_horizontal_resistencia)/fuerza_max_vertical_resistencia, 2)
    e_max_resistencia = params['e_max_resistencia'] = round(ancho_estribo / 2 - d_max_resistencia, 2)
    carga_pilote_ejea_max_resistencia = params['carga_pilote_ejea_max_resistencia'] = round(fuerza_max_vertical_resistencia/num_pilotes + (fuerza_max_vertical_resistencia * e_max_resistencia * distancia_pilote_cg / (num_pilotes * distancia_pilote_cg**2)),2)
    carga_pilote_ejeb_max_resistencia = params['carga_pilote_ejeb_max_resistencia'] = round(fuerza_max_vertical_resistencia/num_pilotes - (fuerza_max_vertical_resistencia * e_max_resistencia * distancia_pilote_cg / (num_pilotes * distancia_pilote_cg**2)),2)
    
    if math.fabs(carga_pilote_ejea_max_resistencia) > math.fabs(resistencia_mayorada_pilote_resistencia) or math.fabs(carga_pilote_ejeb_max_resistencia) > math.fabs(resistencia_mayorada_pilote_resistencia):
       print('no cumple carga vertical sobre pilote para el estado límite de resistencia, caso máximo')
   
    
    d_min_resistencia = params['d_min_resistencia'] = round((momento_min_vertical_resistencia - momento_min_horizontal_resistencia)/fuerza_min_vertical_resistencia, 2)
    e_min_resistencia = params['e_min_resistencia'] = round(ancho_estribo / 2 - d_min_resistencia, 2)
    carga_pilote_ejea_min_resistencia = params['carga_pilote_ejea_min_resistencia'] = round(fuerza_min_vertical_resistencia/num_pilotes + (fuerza_min_vertical_resistencia * e_min_resistencia * distancia_pilote_cg / (num_pilotes * distancia_pilote_cg**2)),2)
    carga_pilote_ejeb_min_resistencia = params['carga_pilote_ejeb_min_resistencia'] = round(fuerza_min_vertical_resistencia/num_pilotes - (fuerza_min_vertical_resistencia * e_min_resistencia * distancia_pilote_cg / (num_pilotes * distancia_pilote_cg**2)),2)
    
    if math.fabs(carga_pilote_ejea_min_resistencia) > math.fabs(resistencia_mayorada_pilote_resistencia) or math.fabs(carga_pilote_ejeb_min_resistencia) > math.fabs(resistencia_mayorada_pilote_resistencia):
       print('no cumple carga vertical sobre pilote para el estado límite de resistencia, caso mínimo')
      
    d_max_eventoextremo = params['d_max_eventoextremo'] = round((momento_max_vertical_eventoextremo - momento_max_horizontal_eventoextremo)/fuerza_max_vertical_eventoextremo, 2)
    e_max_eventoextremo = params['e_max_eventoextremo'] = round(ancho_estribo / 2 - d_max_eventoextremo, 2)
    carga_pilote_ejea_max_eventoextremo = params['carga_pilote_ejea_max_eventoextremo'] = round(fuerza_max_vertical_eventoextremo/num_pilotes + (fuerza_max_vertical_eventoextremo * e_max_eventoextremo * distancia_pilote_cg / (num_pilotes * distancia_pilote_cg**2)),2)
    carga_pilote_ejeb_max_eventoextremo = params['carga_pilote_ejeb_max_eventoextremo'] = round(fuerza_max_vertical_eventoextremo/num_pilotes - (fuerza_max_vertical_eventoextremo * e_max_eventoextremo * distancia_pilote_cg / (num_pilotes * distancia_pilote_cg**2)),2)
    
    if math.fabs(carga_pilote_ejea_max_eventoextremo) > math.fabs(resistencia_mayorada_pilote_eventoextremo): 
       print('no cumple carga vertical sobre pilote para el estado límite de evento extremo, caso máximo, eje a')
    elif math.fabs(carga_pilote_ejeb_max_eventoextremo) > math.fabs(resistencia_mayorada_pilote_levantamiento):
        print('no cumple carga vertical sobre pilote para el estado límite de evento extremo, caso máximo, eje b')

    d_min_eventoextremo = params['d_min_eventoextremo'] = round((momento_min_vertical_eventoextremo - momento_min_horizontal_eventoextremo)/fuerza_min_vertical_eventoextremo, 2)
    e_min_eventoextremo = params['e_min_eventoextremo'] = round(ancho_estribo / 2 - d_min_eventoextremo, 2)
    carga_pilote_ejea_min_eventoextremo = params['carga_pilote_ejea_min_eventoextremo'] = round(fuerza_min_vertical_eventoextremo/num_pilotes + (fuerza_min_vertical_eventoextremo * e_min_eventoextremo * distancia_pilote_cg / (num_pilotes * distancia_pilote_cg**2)),2)
    carga_pilote_ejeb_min_eventoextremo = params['carga_pilote_ejeb_min_eventoextremo'] = round(fuerza_min_vertical_eventoextremo/num_pilotes - (fuerza_min_vertical_eventoextremo * e_min_eventoextremo * distancia_pilote_cg / (num_pilotes * distancia_pilote_cg**2)),2)
    
    if math.fabs(carga_pilote_ejea_min_eventoextremo) > math.fabs(resistencia_mayorada_pilote_eventoextremo): 
       print('no cumple carga vertical sobre pilote para el estado límite de evento extremo, caso mínimo, eje a')
    elif  math.fabs(carga_pilote_ejeb_min_eventoextremo) > math.fabs(resistencia_mayorada_pilote_levantamiento):
        print('no cumple carga vertical sobre pilote para el estado límite de evento extremo, caso mínimo, eje b')

    d_servicio = params['d_servicio'] = round((momento_vertical_servicio - momento_horizontal_servicio)/fuerza_vertical_servicio, 2)
    e_servicio = params['e_servicio'] = round(ancho_estribo / 2 - d_servicio, 2)
    carga_pilote_ejea_servicio = params['carga_pilote_ejea_servicio'] = round(fuerza_vertical_servicio/num_pilotes + (fuerza_vertical_servicio * e_servicio * distancia_pilote_cg / (num_pilotes * distancia_pilote_cg**2)),2)
    carga_pilote_ejeb_servicio = params['carga_pilote_ejeb_servicio'] = round(fuerza_vertical_servicio/num_pilotes - (fuerza_vertical_servicio * e_servicio * distancia_pilote_cg / (num_pilotes * distancia_pilote_cg**2)),2)
    
    if math.fabs(carga_pilote_ejea_servicio) > math.fabs(resistencia_mayorada_pilote_servicio) or math.fabs(carga_pilote_ejeb_servicio) > math.fabs(resistencia_mayorada_pilote_servicio):
       print('no cumple carga vertical sobre pilote para el estado límite de evento servicio')
    
    # Diseño Pilotes
    # fuerza horizontal_numpilotes: Solicitud máxima de fuerza horizontal sobre el conjunto de pilotes, kN
    # fuerza_horizontal_pilote: Fuerza horizontal resistida por cada pilote, kN
    # distancia_entre_pilotes: distancia entre centro a centro de los pilotes, m

    if fuerza_max_horizontal_resistencia > fuerza_max_horizontal_eventoextremo and fuerza_max_horizontal_resistencia >fuerza_horizontal_servicio:
        fuerza_horizontal_numpilotes = fuerza_max_horizontal_resistencia
    elif fuerza_max_horizontal_eventoextremo > fuerza_max_horizontal_resistencia and fuerza_max_horizontal_eventoextremo > fuerza_horizontal_servicio:
         fuerza_horizontal_numpilotes = fuerza_max_horizontal_eventoextremo
    elif fuerza_horizontal_servicio > fuerza_max_horizontal_resistencia and fuerza_horizontal_servicio > fuerza_max_horizontal_eventoextremo:
        fuerza_horizontal_numpilotes = fuerza_horizontal_servicio
    
    params['fuerza_horizontal_numpilotes'] = fuerza_horizontal_numpilotes

    fuerza_horizontal_pilote = params['fuerza_horizontal_pilote'] = round(fuerza_horizontal_numpilotes / num_pilotes, 2)
    
    distancia_entre_pilotes = params['distancia_entre_pilotes'] = params.get('distancia_entre_pilotes', 2.4)
    # Armadura longitudinal en el pilote vaciado in situ

    recub_pilote = params['recub_pilote'] = params.get('recub_pilote', 0.05) #5.12.3-1
    diametro_pilote = params['diametro_pilote'] = params.get('diametro_pilote', 0.8)
    tipo_pilote = params['tipo_pilote'] = params.get('tipo_pilote','prefabricado') 
    area_pilote = params['area_pilote'] = round(math.pi /4 * diametro_pilote ** 2,2)
    if tipo_pilote == 'in situ' :
        if area_pilote < 0.0645 :
            print('no cumple area minima de pilote in situ')
    elif tipo_pilote == 'prefabricado' :
        if area_pilote < 0.09 :
            print('no cumple area minima de pilote prefabricado')
    
    diametro_barras_helicoidal_pilote = params['diametro_barras_helicoidal_pilote'] = params.get('diametro_barras_helicoidal_pilote', 0.0127)
    diametro_barras_longitudinal_pilote = params['diametro_barras_longitudinal_pilote'] = params.get('diametro_barras_longitudinal_pilote', 0.0222)
    dr = params['dr'] = diametro_pilote - 2 *(recub_pilote + diametro_barras_helicoidal_pilote + 0.5 * diametro_barras_longitudinal_pilote)
    de_pilote = params['de_pilote'] = round(diametro_pilote/2 + dr / math.pi, 2)
    dv_pilote = params['dv_pilote'] = round(0.9 * de_pilote,2)
    
    # Verificación de la armadura transversal a cortante del pilote para la minima fuerza de compresión
    # phi_cortante: factor de resistencia phi para cortante
    # area_refuerzo_longitudinal_pilote: área de refuerzo longitudinal del pilote teniendo en cuenta las exigencias dadas para el tipo de pilote y la zona de desempeño sismico, Art. 5.13.4.6, m2
    # area_refuerzo_transversal_pilote: área de refuerzo transversal (helicoidal) del pilote teniendo en cuenta las exigencias dadas para el tipo de pilote y la zona de desempeño sismico, Art. 5.13.4.6, m2
    # fuerzas_compresion_pilote: fuerzas de verticales de compresion que actuan sobre el pilote (positivas según convención de signos), kN
    # fuera_min_compresion_pilote: fuerza mínima de compresión que actúa sobre el pilote, kN    
    # deform_unit_concreto_pilotes_[]n : deformación unitaria del concreto para el caso de verificación,  Art 3.8.3.4.2-4
    # tetha_arm_transversal_[]: ángulo tetha para el caso de verficación, Art 5.8.3.4.2-3, Grados 
    # beta_arm_transversal_[]: ángulo beta para el caso de verificación, Art 5.8.3.4.2-1, Grados
    # Vc_arm_transversal_[]: Fuerza cortante resistida por el concreto para el caso de verificación, Art 5.8.3.3-3, kN
    # Vs_arm_transversal_[]: Fuerza cortante resistida por el acero para el caso de verificación, Art 5.8.3.3-1, kN
    # alfa_arm_transversal: ángulo de inclinación entre el refuerzo transversal y el eje longitudinal, Grados
    # S_arm_transversal_[]: separación del refuerzo transversal,  Art 5.8.3.3-4 , m
    
    
    phi_cortante = params['phi_cortante'] = params.get('phi_cortante', 0.9)
    area_refuerzo_longitudinal_pilote = params['area_refuerzo_longitudinal_pilote'] = params.get('area_refuerzo_longitudinal_pilote', 10*0.000389)
    area_refuerzo_transversal_pilote = params['area_refuerzo_transversal_pilote'] = params.get('area_refuerzo_transversal_pilote', 0.000129)
    cargas_ejeb_pilotes = [carga_pilote_ejeb_max_resistencia, carga_pilote_ejeb_min_resistencia, carga_pilote_ejeb_max_eventoextremo ,carga_pilote_ejeb_min_eventoextremo , carga_pilote_ejeb_servicio]
    fuerzas_compresion_pilotes = [x for x in cargas_ejeb_pilotes if x > 0 ]
    fuerza_min_compresion_pilote = params['fuerza_min_compresion_pilote'] = min(fuerzas_compresion_pilotes)

    deform_unit_concreto_pilotes_min_compresion = params['deform_unit_concreto_pilotes_min_compresion'] = (-0.5 * fuerza_min_compresion_pilote + fuerza_horizontal_pilote)/(E_acero *1000 * area_refuerzo_longitudinal_pilote)
    
    if deform_unit_concreto_pilotes_min_compresion < 0:
        deform_unit_concreto_pilotes_min_compresion = params['deform_unit_concreto_pilotes_min_compresion'] = 0
    
    tetha_arm_transversal_min_compresion = params['tetha_arm_transversal_min_compresion'] = 29 + 3500 * deform_unit_concreto_pilotes_min_compresion
    beta_arm_transversal_min_compresion = params['beta_arm_transversal_min_compresion'] = 4.8/(1+750*deform_unit_concreto_pilotes_min_compresion)
    Vc_arm_transversal_min_compresion = params['Vc_arm_transversal_min_compresion'] = 0.083 * beta_arm_transversal_min_compresion * fc_estribo ** 0.5 * diametro_pilote * dv_pilote * 1000
    Vs_arm_transversal_min_compresion = params['Vs_arm_transversal_min_compresion'] = fuerza_horizontal_pilote / phi_cortante - Vc_arm_transversal_min_compresion
    alfa_arm_transversal = params['alfa_arm_transversal'] = params.get('alfa_arm_transversal', 90)
    S_arm_transversal_min_compresion = params['S_arm_transversal_min_compresion'] = fy * dv_pilote * area_refuerzo_transversal_pilote *2  *(1/math.tan(math.radians(tetha_arm_transversal_min_compresion))+ 1/math.tan(math.radians(alfa_arm_transversal)))* math.sin(math.radians(alfa_arm_transversal)) / (Vs_arm_transversal_min_compresion/1000)

    # Verificación de la armadura transversal a cortante del pilote para la maxima fuerza de compresión

    cargas_ejea_pilotes = [carga_pilote_ejea_max_resistencia, carga_pilote_ejea_min_resistencia, carga_pilote_ejea_max_eventoextremo ,carga_pilote_ejea_min_eventoextremo , carga_pilote_ejea_servicio]
    fuerzas_compresion_pilotes = [x for x in cargas_ejea_pilotes if x > 0 ]
    fuerza_max_compresion_pilote = params['fuerza_max_compresion_pilote'] = max(fuerzas_compresion_pilotes)

    deform_unit_concreto_pilotes_max_compresion = params['deform_unit_concreto_pilotes_max_compresion'] = (-0.5 * fuerza_max_compresion_pilote + fuerza_horizontal_pilote)/(E_acero *1000 * area_refuerzo_longitudinal_pilote)
    if deform_unit_concreto_pilotes_max_compresion < 0:
        deform_unit_concreto_pilotes_max_compresion = params['deform_unit_concreto_pilotes_max_compresion'] = 0
     
    tetha_arm_transversal_max_compresion = params['tetha_arm_transversal_max_compresion'] = 29 + 3500 * deform_unit_concreto_pilotes_max_compresion
    beta_arm_transversal_max_compresion = params['beta_arm_transversal_max_compresion'] = 4.8/(1+750*deform_unit_concreto_pilotes_max_compresion)
    Vc_arm_transversal_max_compresion = params['Vc_arm_transversal_max_compresion'] = 0.083 * beta_arm_transversal_max_compresion * fc_estribo ** 0.5 * diametro_pilote * dv_pilote * 1000
    Vs_arm_transversal_max_compresion = params['Vs_arm_transversal_max_compresion'] = fuerza_horizontal_pilote / phi_cortante - Vc_arm_transversal_max_compresion
    S_arm_transversal_max_compresion = params['S_arm_transversal_max_compresion'] = fy * dv_pilote * area_refuerzo_transversal_pilote *2 *(1/math.tan(math.radians(tetha_arm_transversal_max_compresion))+ 1/math.tan(math.radians(alfa_arm_transversal)))* math.sin(math.radians(alfa_arm_transversal)) / (Vs_arm_transversal_max_compresion/1000)

    # Verificación de la armadura transversal a cortante del pilote para la maxima fuerza de tracción

    cargas_ejeb_pilotes = [carga_pilote_ejeb_max_resistencia, carga_pilote_ejeb_min_resistencia, carga_pilote_ejeb_max_eventoextremo ,carga_pilote_ejeb_min_eventoextremo , carga_pilote_ejeb_servicio]
    fuerzas_traccion_pilotes = [x for x in cargas_ejeb_pilotes if x < 0 ]
    fuerza_max_traccion_pilote = params['fuerza_max_traccion_pilote'] = min(fuerzas_traccion_pilotes)
    
    deform_unit_concreto_pilotes_max_traccion = params['deform_unit_concreto_pilotes_max_traccion'] = (-0.5 * fuerza_max_traccion_pilote + fuerza_horizontal_pilote)/(E_acero *1000 * area_refuerzo_longitudinal_pilote)
    if deform_unit_concreto_pilotes_max_traccion < 0:
        deform_unit_concreto_pilotes_max_traccion = params['deform_unit_concreto_pilotes_max_traccion'] = 0
     
    tetha_arm_transversal_max_traccion = params['tetha_arm_transversal_max_traccion'] = 29 + 3500 * deform_unit_concreto_pilotes_max_traccion
    beta_arm_transversal_max_traccion = params['beta_arm_transversal_max_traccion'] = 4.8/(1+750*deform_unit_concreto_pilotes_max_traccion)
    Vc_arm_transversal_max_traccion = params['Vc_arm_transversal_max_traccion'] = 0.083 * beta_arm_transversal_max_traccion * fc_estribo ** 0.5 * diametro_pilote * dv_pilote * 1000
    Vs_arm_transversal_max_traccion = params['Vs_arm_transversal_max_traccion'] = fuerza_horizontal_pilote / phi_cortante - Vc_arm_transversal_max_traccion
    S_arm_transversal_max_traccion = params['S_arm_transversal_max_traccion'] = fy * dv_pilote * area_refuerzo_transversal_pilote *2 *(1/math.tan(math.radians(tetha_arm_transversal_max_traccion))+ 1/math.tan(math.radians(alfa_arm_transversal)))* math.sin(math.radians(alfa_arm_transversal)) / (Vs_arm_transversal_max_traccion/1000)    

    # Requisitos de refuerzo transversal mínimo

    # S_zonaconfinada: Separación mínima para la zona confinada según lo especififcado en Art 5.13.4.6, m
    # S_zonanoconfinada: Separación mínima para la zona no confinada según lo especififcado en Art 5.13.4.6, m

    S_zonaconfinada = params['S_zonaconfinada'] = params.get('S_zonaconfinada', 0.075)
    S_zonanoconfinada = params['S_zonanoconfinada'] = params.get('S_zonanoconfinada', 0.225)

    # Verificaciones del refuerzo minimo a cortante
    
    # area_refuerzo_transversal_min_pilote_[]: área de refuerzo transversal mínimo para la zona especificada, Art 5.8.2.5-1 ,m2
      
    area_refuerzo_transversal_min_pilote_zonaconfinada = params['area_refuerzo_transversal_min_pilote_zonaconfinada'] = 0.083 * fc_estribo ** 0.5 * S_zonaconfinada * diametro_pilote / fy
    area_refuerzo_transversal_min_pilote_zonanoconfinada = params['area_refuerzo_transversal_min_pilote_zonanoconfinada'] = 0.083 * fc_estribo ** 0.5 * S_zonanoconfinada * diametro_pilote / fy
    if area_refuerzo_transversal_pilote * 2 < area_refuerzo_transversal_min_pilote_zonaconfinada:
        print(' no cumple área mínima de refuerzo a cortante en zona confinada')
    if area_refuerzo_transversal_pilote * 2< area_refuerzo_transversal_min_pilote_zonanoconfinada:
        print(' no cumple área mínima de refuerzo a cortante en zona no confinada')
    
    # cuantía volumetrica


    dc_helicoidal = params['dc_helicoidal'] = round(diametro_pilote - 2 * recub_pilote, 2)

    Lr_helicoidal = params['Lr_helicoidal'] = round((S_zonaconfinada **2 + (math.pi*dc_helicoidal)**2) ** 0.5, 2)

    cuantia_volumetrica = params['cuantia_volumetrica'] = round((area_refuerzo_transversal_pilote * Lr_helicoidal) / (((math.pi * dc_helicoidal **2 )/ 4)* S_zonaconfinada),5)

    cuantia_volumetrica_min_1 = params['cuantia_volumetrica_min_1'] = round(0.12 * fc_estribo / fy, 5) 

    cuantia_volumetrica_min_2 = params['cuantia_volumetrica_min_2'] = round( 0.45 * (diametro_pilote ** 2 / dc_helicoidal ** 2 - 1)* fc_estribo / fy ,5)

    if cuantia_volumetrica < cuantia_volumetrica_min_1 :
        print('no cumple cuantía volumétrica mínima 5.10.11.4.1d')
    elif cuantia_volumetrica < cuantia_volumetrica_min_2 :
        print('no cumple cuantía volumétrica mínima 5.7.4.6')

    # Diseño a flexión de la zapata del estribo

    # Diseño de la armadura de la zapata 
    # Diseño de la zarpa trasera de la zapata
    # Mu_flexion_[]: Momento último de diseño de la zarpa delantera en la unión zarpa delantera con el vástago, kNm/m
    # Mu_flexion_diseño_[]: Momento de diseño escogido como el menor entre MCR_vastago y Mu_flexion_zarpa_delantera segun Art 5.7.3.3.2, kNm/m
    
    
    ## recub_zapata: recubrimiento de concreto de la zapata, m
    # phi_zapata: factor phi utilizado en la ecuación de la cuantía.
    # d_zapata: distancia desde la cara superior hasta el centroide del acero a tracción, m
    # cuantía_[]: Cuantia de acero a flexión para la zarpa delantera.
    # As_flexion_[]: Área de acero para flexión por m de ancho de la zarpa delantera, cm2
    # As_8: Área de una barra #8, cm2.
    # No_barras_flexion_[]: Número de barras #5 necesarias para cumplir el área de acero requerida. 
    # separacion_flexion_[]: Separación entre barras en la zarpa delantera para el diseño a flexión, cm
   
    DC_relleno_m = params['DC_relleno_m'] = DC_relleno / largo_estribo
    M_c_relleno = params['M_c_relleno'] = DC_relleno_m * 0.5 * ancho_aletas
    DC_talon_m = params['DC_talon_m'] = (altura_talon*ancho_talon*pesoespecifico_concreto)
    M_c_talon = params['M_c_talon'] = DC_talon_m * 0.5 * ancho_aletas

    Mu_flexion_zarpa_trasera_resistencia = params['Mu_flexion_zarpa_trasera_resistencia'] = round(factor_carga_EV_MyE_max * M_c_relleno  + factor_carga_DC_max *M_c_talon , 2)
    Mu_flexion_zarpa_trasera_eventoextremo = params['Mu_flexion_zarpa_trasera_eventoextremo'] = round(factor_carga_EV_MyE_max * M_c_relleno + factor_carga_DC_max *M_c_talon + math.fabs(fuerza_max_traccion_pilote * 1 / distancia_entre_pilotes) , 2)
    
    if Mu_flexion_zarpa_trasera_resistencia > Mu_flexion_zarpa_trasera_eventoextremo:
        Mu_flexion_zarpa_trasera = Mu_flexion_zarpa_trasera_resistencia
    else :
        Mu_flexion_zarpa_trasera = Mu_flexion_zarpa_trasera_eventoextremo
    

    params['Mu_flexion_zarpa_trasera'] = Mu_flexion_zarpa_trasera 
    

    # gamma_3: relación entre la resistencia especificada a fluencia y la resistencia última a tracción del refuerzo. Art 5.7.3.3.2
    # gamma_1: factor de variación de la fisuración por flexión, Art 5.7.3.3.2
    # fr: Módulo de rotura del concreto en el vástago, Art 5.4.2.6, MPa
    # Sc_[]: Módulo de sección para la fibra extrema de la sección compuesta donde el esfuerzo es causado por las cargas externas. m3 
    # MCR_[]: Momento de verificación de refuerzo mínimo, Art 5.7.3.3.2, kNm
    
    gamma_3 = params['gamma_3'] = params.get('gamma_3', 0.75)
    gamma_1 = params['gamma_1'] = params.get('gamma_1', 1.6)
    fr = params['fr'] = round(0.62 * (fc_estribo)**0.5, 2)
    Sc_zarpa_trasera = params['Sc_zarpa_trasera'] = round(1*((altura_base + altura_talon)/2) ** 2 / 6, 2)
    MCR_zarpa_trasera = params['MCR_zarpa_trasera'] = round(gamma_3 * (gamma_1 ** 2 * fr * Sc_zarpa_trasera)*1000, 2)

    if MCR_zarpa_trasera < 1.33 * Mu_flexion_zarpa_trasera:
        Mu_diseño_flexion_zarpa_trasera = MCR_zarpa_trasera
    else :
        Mu_diseño_flexion_zarpa_trasera = 1.33 * Mu_flexion_zarpa_trasera

    params['Mu_diseño_flexion_zarpa_trasera'] = Mu_diseño_flexion_zarpa_trasera

    
    recub_zapata = params['recub_zapata'] = params.get('recub_zapata', 0.1)
    phi_zapata = params['phi_zapata'] = params.get('phi_zapata', 0.9)
    d_zapata = params['d_zapata'] = round( altura_talon - recub_zapata ,2)
    cuantia_zarpa_trasera_flexion = params['cuantia_zarpa_trasera_flexion'] = round((1-(1-(2 * Mu_diseño_flexion_zarpa_trasera / (phi_zapata * 1 * d_zapata ** 2 * 0.85 * fc_estribo *1000))) ** 0.5) * 0.85* fc_estribo / fy , 5)
    As_flexion_zarpa_trasera = params['As_flexion_zarpa_trasera'] = round(cuantia_zarpa_trasera_flexion * d_zapata *100 * 100, 2)
    As_8 = params['As_8'] = 5.1
    No_barras_flexion_zarpa_trasera = params['No_barras_flexion_zarpa_trasera'] = math.ceil(As_flexion_zarpa_trasera / As_8)
    separacion_flexion_zarpa_trasera = params['separacion_flexion_zarpa_trasera'] = round(100/ No_barras_flexion_zarpa_trasera)
    
    deform_unit_concreto_compresion_zapata = params['deform_unit_concreto_compresion_zapata'] = params.get('deform_unit_concreto_compresion_zapata', 0.003)
    c_zarpa_trasera = params['c_zarpa_trasera'] = As_flexion_zarpa_trasera/10000 * fy /( 0.85 * fc_estribo * 1 * 0.85)
    deform_unit_total_zarpa_trasera = params['deform_unit_total_zarpa_trasera'] = (d_zapata - c_zarpa_trasera) * (deform_unit_concreto_compresion_zapata / c_zarpa_trasera)
    if deform_unit_total_zarpa_trasera < 0.005:
        print('revisar phi zapata, deformación unitaria total =', deform_unit_total_zarpa_trasera)

    # Diseño de la zarpa delantera
    

    Mu_flexion_zarpa_delantera = params['Mu_flexion_zarpa_delantera'] = fuerza_max_compresion_pilote * (ancho_base - espesor_vastago - diametro_pilote) / distancia_entre_pilotes
    
    Sc_zarpa_delantera = params['Sc_zarpa_delantera'] = round(1*((altura_base + altura_talon)/2) ** 2 / 6, 2)
    MCR_zarpa_delantera = params['MCR_zarpa_delantera'] = round(gamma_3 * (gamma_1 ** 2 * fr * Sc_zarpa_delantera)*1000, 2)

    if MCR_zarpa_delantera < 1.33 * Mu_flexion_zarpa_delantera:
        Mu_diseño_flexion_zarpa_delantera = MCR_zarpa_delantera
    else :
        Mu_diseño_flexion_zarpa_delantera = 1.33 * Mu_flexion_zarpa_delantera

    params['Mu_diseño_flexion_zarpa_delantera'] = Mu_diseño_flexion_zarpa_delantera

    cuantia_zarpa_delantera_flexion = params['cuantia_zarpa_delantera_flexion'] = round((1-(1-(2 * Mu_diseño_flexion_zarpa_delantera / (phi_zapata * 1 * d_zapata ** 2 * 0.85 * fc_estribo *1000))) ** 0.5) * 0.85* fc_estribo / fy , 5)
    As_flexion_zarpa_delantera = params['As_flexion_zarpa_delantera'] = round(cuantia_zarpa_delantera_flexion * d_zapata *100 * 100, 2)
    As_8 = params['As_8'] = 5.1
    No_barras_flexion_zarpa_delantera = params['No_barras_flexion_zarpa_delantera'] = math.ceil(As_flexion_zarpa_delantera / As_8)
    separacion_flexion_zarpa_delantera = params['separacion_flexion_zarpa_delantera'] = round(100/ No_barras_flexion_zarpa_delantera)
    
    deform_unit_concreto_compresion_zapata = params['deform_unit_concreto_compresion_zapata'] = params.get('deform_unit_concreto_compresion_zapata', 0.003)
    c_zarpa_delantera = params['c_zarpa_delantera'] = As_flexion_zarpa_delantera /10000 * fy /( 0.85 * fc_estribo * 1 * 0.85)
    deform_unit_total_zarpa_delantera = params['deform_unit_total_zarpa_delantera'] = (d_zapata - c_zarpa_delantera) * (deform_unit_concreto_compresion_zapata / c_zarpa_delantera)
    if deform_unit_total_zarpa_delantera < 0.005:
        print('revisar phi zapata, deformación unitaria total =', deform_unit_total_zarpa_delantera)

    # Diseño de la armadura transversal de la zapata
    # Wu_zapata: Resultante de cargas verticales dividida en la longitud de la zapata, kN/m
    # Mu_transversal_zapata: Momento último que actúa sobre la zapata, tomado de un analisis en el que la zapata es una viga apoyada sobre los pilotes, kNm/m

    Wu_zapata = params['Wu_zapata'] = (max(fuerza_max_vertical_resistencia, fuerza_max_vertical_eventoextremo, fuerza_vertical_servicio))/ largo_estribo
    
    Mu_transversal_zapata = params['Mu_transversal_zapata'] = params.get('Mu_transversal_zapata', 667.08)

    Sc_transversal_zapata = params['Sc_transversal_zapata'] = round(ancho_estribo *((altura_base + altura_talon)/2) ** 2 / 6, 2)
    MCR_transversal_zapata = params['MCR_transversal_zapata'] = round(gamma_3 * (gamma_1 ** 2 * fr * Sc_transversal_zapata)*1000, 2)

    if MCR_transversal_zapata < 1.33 * Mu_transversal_zapata:
        Mu_diseño_transversal_zapata = MCR_transversal_zapata
    else :
        Mu_diseño_transversal_zapata = 1.33 * Mu_transversal_zapata

    params['Mu_diseño_transversal_zapata'] = Mu_diseño_transversal_zapata

    cuantia_transversal_zapata = params['cuantia_transversal_zapata'] = round((1-(1-(2 * Mu_diseño_transversal_zapata / (phi_zapata * ancho_estribo * d_zapata ** 2 * 0.85 * fc_estribo *1000))) ** 0.5) * 0.85* fc_estribo / fy , 5)
    As_flexion_transversal_zapata = params['As_flexion_transversal_zapata'] = round(cuantia_transversal_zapata * d_zapata *100 * ancho_estribo *100, 2)
    As_8 = params['As_8'] = 5.1
    No_barras_transversal_zapata = params['No_barras_transversal_zapata'] = math.ceil(As_flexion_transversal_zapata / As_8)
    separacion_transversal_zapata = params['separacion_transversal_zapata'] = round(100/ No_barras_transversal_zapata)
    

    # Verificación a cortante de la zapata

    # Acción en una dirección, Art 5.13.3.6.2, Zapata como viga
    # 
    # a_zapata_viga: profundidad del bloque de compresiones del concreto en el analisis de la zapata como viga, m
    # dv_zapata_viga: brazo interno de palanca del par tracción compresión en ele analisis de la zapata como viga, m
    # Dc_talon_m: Carga del peso del talón por m de largo, kN/m
    # Pu_zapata_viga: Fuerza cortante en la interfaz zapata - vástago del estribo, en una longitud de la distancia de separación entre pilotes, kN
    # beta_zapata_viga: factor beta especififcado en Art. 5.8.3.4.1
    # Vn_zapata_viga: Máxima fuerza cortante nominal de acuerdo con Art. 5.8.3.3, kN
    # Vc_zapata_viga: Fuerza cortante nominal resistida por el concreto, kN
    # Vu_zapata_viga: Fuerza cortante última resistida por el concreto

    a_zapata_viga = params['a_zapata_viga'] = As_flexion_zarpa_delantera/10000 * fy/(0.85*1*fc_estribo)
    dv_zapata_viga = params['dv_zapata_viga'] = d_zapata -a_zapata_viga/2
    DC_talon_m = params['DC_talon_m'] = altura_talon * ancho_talon * pesoespecifico_concreto

    Pu_zapata_viga = params['Pu_zapata_viga'] = factor_carga_DC_max * DC_talon_m * distancia_entre_pilotes + factor_carga_EV_MyE_max * DC_relleno_m * distancia_entre_pilotes + math.fabs(fuerza_max_traccion_pilote)
    
    
    if ancho_talon < 3 * dv_zapata_viga:
        beta_zapata_viga = 2
        tetha_zapata_viga = 45
    else :
        print('revisar factor beta en diseño a cortante de la zapata, caso zapata-viga, Art. 5.8.3.4.1')
    
    params['beta_zapata_viga'] = beta_zapata_viga

    Vn_zapata_viga = params['Vn_zapata_viga'] = 0.25*fc_estribo* distancia_entre_pilotes* dv_zapata_viga * 1000
    Vc_zapata_viga = params['Vc_zapata_viga'] = 0.083 * beta_zapata_viga * fc_estribo **0.5 *distancia_entre_pilotes * dv_zapata_viga *1000
    Vu_zapata_viga = params['Vu_zapata_viga'] = 0.9 * Vc_zapata_viga 
    
    if Vu_zapata_viga < Pu_zapata_viga:
        print('se requieren estribos para resistir la fuerza cortante sobre la zapata')
        As_cortante_zapata_viga = params['As_cortante_zapata_viga'] = params.get('As_cortante_zapata_viga', 2*0.000129)
        Vs_zapata_viga = params['Vs_zapata_viga'] = Pu_zapata_viga/phi_cortante - Vc_zapata_viga
        S_arm_cortante_zapata_viga = params['S_arm_cortante_zapata_viga'] = fy *1000 * dv_zapata_viga * As_cortante_zapata_viga * 1 / math.tan(math.radians(tetha_zapata_viga)) / Vs_zapata_viga
        print('separación de refuerzo a cortante de 2 barras #4 = ',S_arm_cortante_zapata_viga)

    # Acción en dos direcciones (5.13.3.6.3), acción como losa
    #
    # bo_zapata_losa: perímetro mínimo de plano de falla a cortante en análisis de zapata como losa, m
    # beta_c_zapata_losa: relación entre el largo del vástago y el espesor del mismo.
    # Vn_zapata_losa: REsistencia nominal del concreto a cortante para la acción en dos direcciones, 5.13.3.6.3-1 , kN
    # Vn_zapata_losa_limite: Límite de resistencia nominal del concreto a cortante para la acción en dos direcciones, Art 5.13.3.6.3-1 ,kN 
    # Vu_zapata_losa: fuerza cortante última resistida por el concreto, kN

    bo_zapata_losa = params['bo_zapata_losa'] = math.pi*( dv_zapata_viga * 0.5 + diametro_pilote / 2) + 2 * diametro_pilote
    beta_c_zapata_losa = params['beta_c_zapata_losa'] = largo_estribo / espesor_vastago
    Vn_zapata_losa = params['Vn_zapata_losa'] = (0.17 + 0.33 / beta_c_zapata_losa) * bo_zapata_losa * dv_zapata_viga * fc_estribo ** 0.5 *1000
    Vn_zapata_losa_limite = params['Vn_zapata_losa_limite'] = 0.33 * bo_zapata_losa * dv_zapata_viga * fc_estribo ** 0.5 *1000

    if Vn_zapata_losa > Vn_zapata_losa_limite : 
        print('no cumple fuerza cortante , acción en dos direcciones, zapata - losa')

    Vu_zapata_losa = params['Vu_zapata_losa'] = 0.9 * Vn_zapata_viga

    if fuerza_max_traccion_pilote > Vu_zapata_losa:
        print('no cumple fuerza cortante para analisis zapata-losa, Vu')

    
    # Diseño a flexion del vástago del estribo

     # Diseño de la armadura interior del vástago

    # EH_vastago: Empuje estático del suelo sobre el vástago, kN/m
    # Y_vastago_EH: Distancia de aplicación de la resultante de EH_vastago desde la unión vástago - zapata. m
    # Y_vastago_pseis: Distancia de aplicación de la fuerza Pseis desde la unión vástago - zapata. m
    # Y_vastago_Hbu: Distancia de aplicación de la fuerza Hbu desde la unión vástago - zapata. m
    # Y_vastago_BR: Distancia de aplicación de la fuerza BR desde la unión vástago - zapata. m
    # Y_vastago_LSy: Distancia de aplicación de fuerza LSy desde la unión vástago - zapata. m
    # M_a_a_[]_vastago: Momento producido por la fuerza [] en la unión vástago zapata, kNm/m


    EH_vastago = params['EH_vastago'] = round(0.5 * coeficiente_presion_lateral_activa_suelo_desf * pesoespecifico_suelo * (altura_estribo - altura_base) ** 2, 2)
    Y_vastago_EH = params['Y_vastago_EH'] = round((altura_estribo - altura_base) / 3 ,2)
    Y_vastago_pseis = params['Y_vastago_pseis'] =round(0.4 * (altura_estribo - altura_base), 2)
    Y_vastago_Hbu = params['Y_vastago_Hbu'] = altura_vastago 
    Y_vastago_BR = params['Y_vastago_BR'] = round(altura_estribo - altura_base + 1.8 , 2)
    L_S_x_vastago = params['L_S_x_vastago'] = round(presion_horizontal_suelo_sobrecargaviva * (altura_estribo - altura_base),2)
    Y_vastago_LSy = params['Y_vastago_LSy'] =round((altura_estribo - altura_base)/2 ,2)
    M_a_a_EH_vastago = params['M_a_a_EH_vastago'] =round(EH_vastago * Y_vastago_EH, 2)
    M_a_a_pseis_vastago = params['M_a_a_pseis_vastago'] = round( Pseis_e/ largo_estribo * Y_vastago_pseis ,2) 
    M_a_a_Hbu_vastago = params['M_a_a_Hbu_vastago'] = round( Hbu / largo_estribo* Y_vastago_Hbu ,2) 
    M_a_a_BR_vastago = params['M_a_a_BR_vastago'] = round( BR_e / largo_estribo * Y_vastago_BR ,2) 
    M_a_a_LSx_vastago = params['M_a_a_LSx_vastago'] = round( L_S_x_vastago * Y_vastago_LSy ,2) 
    
    # Momento mayorado Evento extemo I
    # Mu_vastago_[]: Momento último de diseño para el estado límite especificado. kNm/m
    # Mu_vastago_diseño: El mayor entre los momentos últimos de resistencia y evento extremo. kNm/m
    # recub_vastago: recubrimiento de concreto del vástago, m
    # phi_vastago: factor phi utilizado en la ecuación de la cuantía.
    # d_vastago: distancia desde la cara superior hasta el centroide del acero a tracción, m
    # cuantía_vastago: Cuantia de acero a flexión para el vástago.
    # As_flexion_vastago: Área de acero para flexión por m de ancho de vástago, cm2
    # As_8: Área de una barra #8, cm2.
    # No_barras_8_flexion_vastago: Número de barras #8 necesarias paea cumplir el área de acero requerida. 
    # separacion_flexion_vastago: Separación entre barras en el vástago para el diseño a flexión, cm

    
    Mu_vastago_eventoextremo = params['Mu_vastago_eventoextremo'] = round(0.5 * (M_a_a_BR_vastago + M_a_a_LSx_vastago) + 1 * (M_a_a_pseis_vastago + M_a_a_Hbu_vastago), 2) 
    Mu_vastago_resistencia = params['Mu_vastago_resistencia'] = round(1.5 * M_a_a_EH_vastago + 1.75 *(M_a_a_LSx_vastago + M_a_a_BR_vastago), 2)

    if Mu_vastago_eventoextremo > Mu_vastago_resistencia:
        Mu_vastago = Mu_vastago_eventoextremo
    else :
        Mu_vastago = Mu_vastago_resistencia
    
    params['Mu_vastago'] = Mu_vastago
    
    Sc_vastago = params['Sc_vastago'] = round(1*espesor_vastago ** 2 / 6, 2)
    MCR_vastago = params['MCR_vastago'] = round(gamma_3 * (gamma_1 ** 2 * fr * Sc_vastago)*1000, 2)
    if MCR_vastago < 1.33 * Mu_vastago:
        Mu_diseño_vastago = MCR_vastago
    else :
        Mu_diseño_vastago = 1.33 * Mu_vastago

    params['Mu_diseño_vastago'] = Mu_diseño_vastago

    
    recub_vastago = params['recub_vastago'] = params.get('recub_vastago', 0.08)
    phi_vastago = params['phi_vastago'] = params.get('phi_vastago', 0.9)
    d_vastago = params['d_vastago'] = round( espesor_vastago - recub_vastago ,2)
   
    cuantia_vastago_flexion = params['cuantia_vastago_flexion'] = round((1-(1-(2 * Mu_diseño_vastago / (phi_vastago * 1 * d_vastago ** 2 * 0.85 * fc_estribo *1000))) ** 0.5) * 0.85* fc_estribo / fy , 5)
    As_flexion_vastago = params['As_flexion_vastago'] = round(cuantia_vastago_flexion * d_vastago *100 * 100, 2)
    As_8 = params['As_8'] = 5.1
    No_barras_8_flexion_vastago = params['No_barras_8_flexion_vastago'] = round(As_flexion_vastago / As_8, 2)
    separacion_flexion_vastago = params['separacion_flexion_vastago'] = round(100/ No_barras_8_flexion_vastago)
    

    c_vastago = params['c_vastago'] = As_flexion_vastago /10000 * fy /( 0.85 * fc_estribo * 1 * 0.85)
    deform_unit_total_vastago = params['deform_unit_total_vastago'] = (d_vastago - c_vastago) * (deform_unit_concreto_compresion_zapata / c_vastago)
    if deform_unit_total_vastago < 0.005:
        print('revisar phi vastago, deformación unitaria total =', deform_unit_total_vastago)
    
    #Armadura por retracción de fraguado y temperatura en el cuerpo del vástago
    #
    # As_retraccionytemperatura_vastago: Área de refuerzo por retracción y temperatura, mm2, Art 5.10.8
    # As_4: Área de una barra #4, cm2
    # No_barras_4_retraccionytemperatura_vastago: Número de barras necesarias para cumplir el refuerzo minimo por retracción de fraguado y temperatura.
    # separacion_retraccionytemperatura_vastago: separación de las barras de refuerzo por retracción de fraguado y temperatura, cm  

    As_retraccionytemperatura_vastago = params['As_retraccionytemperatura_vastago'] = round(750 * altura_vastago * espesor_vastago *1000 /( 2 * (altura_vastago + espesor_vastago) * fy),2)
    if As_retraccionytemperatura_vastago < 234 or As_retraccionytemperatura_vastago > 1278 :
        print( 'no cumple armadura por retracción y temperatura' )
    As_5 = params['As_5'] = 1.99
    No_barras_4_retraccionytemperatura_vastago = params['No_barras_4_retraccionytemperatura_vastago'] = (As_retraccionytemperatura_vastago /100 / As_5)
    separacion_retraccionytemperatura_vastago = params['separacion_retraccionytemperatura_vastago'] = round(100 / No_barras_4_retraccionytemperatura_vastago, 2)

    

    # Control de agrietamiento del acero del vástago

    # gamma_e_vastago: Factor de exposición según Art 5.7.3.4
    #
    # relacionmodular_estribo: relación entre el módulo de elasticidad del acero y el modulo de elasticidad del concreto
    # M_servicio_vastago: Momento para el estado límite de servicio, kNm/m
    # X_ejecentroidal_vastago: Posición del eje centroidal de la sección transformada, m
    # I_vastago: Momento centroidal de inercia de la sección transformada, m4
    # fss_vastago: Esfuerzo actuante sobre el acero de refuerzo, MPa
    # beta_s_vastago: coeficiente definido en Art 5.7.3.4-1
    # separacion_maxima_agrietamiento_vastago: Separación máxima del refuerzo a tracción, Art 5.7.3.4, cm.


    gamma_e_vastago = params['gamma_e_vastago'] = params.get('gamma_e_vastago', 1)
    relacionmodular_estribo = params['relacionmodular_estribo'] = round(E_acero / (4800 * (fc_estribo)** 0.5))   
    M_servicio_vastago =params['M_servicio_vastago']= M_a_a_EH_vastago + 1 * (M_a_a_BR_vastago + M_a_a_LSx_vastago) 
    X_ejecentroidal_vastago = params['X_ejecentroidal_vastago'] = round(- 2 * relacionmodular_estribo * As_flexion_vastago /10000 + ((2 * relacionmodular_estribo * As_flexion_vastago /10000)**2 - 4 * 1* -2 * relacionmodular_estribo * As_flexion_vastago /10000 *d_vastago)**0.5 /( 2 * 1),2)
    I_vastago = params['I_vastago'] = round(1 * X_ejecentroidal_vastago ** 3 / 3 + relacionmodular_estribo * As_flexion_vastago /10000 * (d_vastago - X_ejecentroidal_vastago) ** 2, 4)
    fss_vastago= params['fss_vastago'] = round(M_servicio_vastago * (d_vastago - X_ejecentroidal_vastago) * relacionmodular_estribo / I_vastago, 2)
    beta_s_vastago = params['beta_s_vastago'] = round(1 +(recub_vastago / (0.7 * (espesor_vastago - recub_vastago))), 2)
    separacion_maxima_agrietamiento_vastago = params['separacion_maxima_agrietamiento_vastago'] = round((123000 * gamma_e_vastago / (beta_s_vastago * fss_vastago/1000) - 2 * recub_vastago)/10, 2) 
    if separacion_maxima_agrietamiento_vastago < separacion_flexion_vastago :
        print('no cumple control de agrietamiento en el vástago')
    
    # Diseño a flexion del espaldar del estribo

     # Diseño de la armadura del espaldar

    # EH_vastago: Empuje estático del suelo sobre el vástago, kN/m
    # Y_vastago_EH: Distancia de aplicación de la resultante de EH_vastago desde la unión vástago - zapata. m
    # Y_vastago_pseis: Distancia de aplicación de la fuerza Pseis desde la unión vástago - zapata. m
    # Y_vastago_Hbu: Distancia de aplicación de la fuerza Hbu desde la unión vástago - zapata. m
    # Y_vastago_BR: Distancia de aplicación de la fuerza BR desde la unión vástago - zapata. m
    # Y_vastago_LSy: Distancia de aplicación de fuerza LSy desde la unión vástago - zapata. m
    # M_a_a_[]_vastago: Momento producido por la fuerza [] en la unión vástago zapata, kNm/m

    
    EH_espaldar = params['EH_vastago'] = round(0.5 * coeficiente_presion_lateral_activa_suelo_desf * pesoespecifico_suelo * (altura_espaldar) ** 2, 2)
    Y_espaldar_EH = params['Y_vastago_EH'] = round((altura_espaldar) / 3 ,2)
  
   
    L_S_x_espaldar = params['L_S_x_espaldar'] = round(presion_horizontal_suelo_sobrecargaviva * (altura_espaldar),2)
    Y_espaldar_LSx = params['Y_espaldar_LSx'] =round((altura_espaldar)/2 ,2)
    M_a_a_EH_espaldar = params['M_a_a_EH_espaldar'] =round(EH_espaldar * Y_espaldar_EH, 2)
   
    M_a_a_LSx_espaldar = params['M_a_a_LSx_espaldar'] = round( L_S_x_espaldar * Y_espaldar_LSx ,2) 
    

    # Momento mayorado Evento extemo I
    # Mu_vastago_[]: Momento último de diseño para el estado límite especificado. kNm/m
    # Mu_vastago_diseño: El mayor entre los momentos últimos de resistencia y evento extremo. kNm/m
    # recub_vastago: recubrimiento de concreto del vástago, m
    # phi_vastago: factor phi utilizado en la ecuación de la cuantía.
    # d_vastago: distancia desde la cara superior hasta el centroide del acero a tracción, m
    # cuantía_vastago: Cuantia de acero a flexión para el vástago.
    # As_flexion_vastago: Área de acero para flexión por m de ancho de vástago, cm2
    # As_8: Área de una barra #8, cm2.
    # No_barras_8_flexion_vastago: Número de barras #8 necesarias paea cumplir el área de acero requerida. 
    # separacion_flexion_vastago: Separación entre barras en el vástago para el diseño a flexión, cm

    Mu_espaldar = params['Mu_espaldar'] = round(1.5 * M_a_a_EH_espaldar + 1.75 *(M_a_a_LSx_espaldar), 2)
    
    Sc_espaldar = params['Sc_espaldar'] = round(altura_espaldar * espesor_espaldar ** 2 / 6, 2)
    MCR_espaldar = params['MCR_espaldar'] = round(gamma_3 * (gamma_1 ** 2 * fr * Sc_espaldar)*1000, 2)
    if MCR_espaldar < 1.33 * Mu_espaldar:
        Mu_diseño_espaldar = MCR_espaldar
    else :
        Mu_diseño_espaldar = 1.33 * Mu_espaldar

    params['Mu_diseño_espaldar'] = Mu_diseño_espaldar

    
    recub_espaldar = params['recub_espaldar'] = params.get('recub_espaldar', 0.1)
    phi_espaldar = params['phi_espaldar'] = params.get('phi_espaldar', 0.9)
    d_espaldar = params['d_espaldar'] = round( espesor_espaldar - recub_espaldar ,2)
   
    cuantia_espaldar_flexion = params['cuantia_espaldar_flexion'] = round((1-(1-(2 * Mu_diseño_espaldar / (phi_espaldar * 1 * d_espaldar ** 2 * 0.85 * fc_estribo *1000))) ** 0.5) * 0.85* fc_estribo / fy , 5)
    As_flexion_espaldar = params['As_flexion_espaldar'] = round(cuantia_espaldar_flexion * d_espaldar *100 * 100, 2)
    As_4 = params['As_8'] = 1.29
    No_barras_8_flexion_espaldar = params['No_barras_8_flexion_espaldar'] = round(As_flexion_espaldar / As_5, 2)
    separacion_flexion_espaldar = params['separacion_flexion_espaldar'] = round(100/ No_barras_8_flexion_espaldar)

    

    #Armadura por retracción de fraguado y temperatura en el cuerpo del espaldar
    #
    # As_retraccionytemperatura_espaldaro: Área de refuerzo por retracción y temperatura, mm2, Art 5.10.8
    # As_4: Área de una barra #4, cm2
    # No_barras_4_retraccionytemperatura_espaldar: Número de barras necesarias para cumplir el refuerzo minimo por retracción de fraguado y temperatura.
    # separacion_retraccionytemperatura_espaldar: separación de las barras de refuerzo por retracción de fraguado y temperatura, cm  

    As_retraccionytemperatura_espaldar = params['As_retraccionytemperatura_espaldar'] = round(750 * altura_espaldar * espesor_espaldar *1000 /( 2 * (altura_espaldar + espesor_espaldar) * fy),2)
    if As_retraccionytemperatura_espaldar < 234 or As_retraccionytemperatura_espaldar > 1278 :
        print( 'no cumple armadura por retracción y temperatura' )

    No_barras_4_retraccionytemperatura_espaldar = params['No_barras_4_retraccionytemperatura_espaldar'] = (As_retraccionytemperatura_espaldar /100 / As_4)
    separacion_retraccionytemperatura_espaldar = params['separacion_retraccionytemperatura_espaldar'] = round(100 / No_barras_4_retraccionytemperatura_espaldar, 2)
    
    return params

if __name__ == '__main__':
    # diseño estribo libro profesor Carlos Vallecilla
    filename = 'test estribo pilotes.docx'
    params = {
     
    } 
    
    params = design(params)
    
    doc.render(params)
    doc.save(filename)