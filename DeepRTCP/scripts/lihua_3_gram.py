

hydrophobicity = ['RKEDQN', 'GASTPHY', 'CVLIMFW']

surface_tension = ['GQDNAHR', 'KTSEC', 'ILMFPWYV']

Solventsolubility = ['ALFCGIVW', 'RKQEND', 'MPSTHY']

charged_polarity = ['LIFWCMVY', 'PATGS', 'HQRKEND']


def main():
    hydro_tension = []
    for a_m_1 in Solventsolubility:
        a_m_1 = list(a_m_1)
        for a_m_2 in charged_polarity:
            a_m_2 = list(a_m_2)
            intersection = list(set(a_m_1).intersection(set(a_m_2)))
            hydro_tension.append(intersection)
    print(hydro_tension)



if __name__ == '__main__':
    main()