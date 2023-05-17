import hero.utils.utils as hero_utils


def genes2rawtraits(genes):
    traits = []

    stat_raw_kai = "".join(hero_utils.__genesToKai(genes).split(' '))
    for ki in range(0, len(stat_raw_kai)):
        kai = stat_raw_kai[ki]
        value_num = hero_utils.__kai2dec(kai)
        traits.append(value_num)
    return traits


def test_real_genes():
    traits = genes2rawtraits(555929484678960990845956674907717182088847150503766919279864685875364224)

    inv_traits = traits.copy()
    inv_traits.reverse()
    split_traits = [traits[i:i + 4] for i in range(0, len(traits), 4)]
    inv_split_traits = [inv_traits[i:i + 4] for i in range(0, len(inv_traits), 4)]
    main_traits = []
    inv_main_traits = []
    for i in range(12):
        main_traits.append(split_traits[i][3])
        inv_main_traits.append(inv_split_traits[i][0])
    print(main_traits)
    print(inv_main_traits)


def test_encode():
    expected_dominant_traits = [9, 9, 0, 2, 4, 4, 6, 0, 2, 2, 8, 0]
    inv_expected_dominant_traits = expected_dominant_traits.copy()
    inv_expected_dominant_traits.reverse()
    expected_traits = [0 for i in range(48)]
    for i in range(12):
        expected_traits[i * 4] = inv_expected_dominant_traits[i]
    genes = hero_utils._encode_traits(expected_traits)
    traits = genes2rawtraits(genes)
    inv_traits = traits.copy()
    inv_traits.reverse()
    split_traits = [traits[i:i + 4] for i in range(0, len(traits), 4)]
    inv_split_traits = [inv_traits[i:i + 4] for i in range(0, len(inv_traits), 4)]
    main_traits = []
    inv_main_traits = []
    for i in range(12):
        main_traits.append(split_traits[i][3])
        inv_main_traits.append(inv_split_traits[i][0])
    print(main_traits)
    print(inv_main_traits)
    assert main_traits == expected_dominant_traits
    assert inv_main_traits == inv_expected_dominant_traits

test_real_genes()
test_encode()