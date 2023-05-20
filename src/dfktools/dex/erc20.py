import sys
from web3 import Web3

SERENDALE_IDS = ['serendale', 'sd']
CRYSTALVALE_IDS = ['crystalvale', 'cv']
SERENDALE2_IDS = ['serendale2', 'sd2']

ITEMS_SERENDALE = [
    ("0x72Cb10C6bfA5624dD07Ef608027E366bd690048F", "JEWEL", "Jewel"),
    ("0xA9cE83507D872C5e1273E745aBcfDa849DAA654F", "XJEWEL", "xJewel"),
    ("0x3a4EDcf3312f44EF027acfd8c21382a5259936e7", "DFKGOLD", "Gold Pile"),
    ("0x24eA0D436d3c2602fbfEfBe6a16bBc304C963D04", "DFKTEARS", "Gaia's Tears"),
    ("0x6e1bC01Cc52D165B357c42042cF608159A2B81c1", "DFKAMBRTFY", "Ambertaffy"),
    ("0x68EA4640C5ce6cC0c9A1F17B7b882cB1cBEACcd7", "DFKDRKWD", "Darkweed"),
    ("0x600541aD6Ce0a8b5dae68f086D46361534D20E80", "DFKGLDVN", "Goldvein"),
    ("0x043F9bd9Bb17dFc90dE3D416422695Dd8fa44486", "DFKRGWD", "Ragweed"),
    ("0x094243DfABfBB3E6F71814618ace53f07362a84c", "DFKRDLF", "Redleaf"),
    ("0x6B10Ad6E3b99090De20bF9f95F960addC35eF3E2", "DFKRCKRT", "Rockroot"),
    ("0xCdfFe898E687E941b124dfB7d24983266492eF1d", "DFKSWFTHSL", "Swift-Thistle"),
    ("0x78aED65A2Cc40C7D8B0dF1554Da60b38AD351432", "DFKBLOATER", "Bloater"),
    ("0xe4Cfee5bF05CeF3418DA74CFB89727D8E4fEE9FA", "DFKIRONSCALE", "Ironscale"),
    ("0x8Bf4A0888451C6b5412bCaD3D9dA3DCf5c6CA7BE", "DFKLANTERNEYE", "Lanterneye"),
    ("0xc5891912718ccFFcC9732D1942cCD98d5934C2e1", "DFKREDGILL", "Redgill"),
    ("0xb80A07e13240C31ec6dc0B5D72Af79d461dA3A70", "DFKSAILFISH", "Sailfish"),
    ("0x372CaF681353758f985597A35266f7b330a2A44D", "DFKSHIMMERSKIN", "Shimmerskin"),
    ("0x2493cfDAcc0f9c07240B5B1C4BE08c62b8eEff69", "DFKSILVERFIN", "Silverfin"),
    ("0x66F5BfD910cd83d3766c4B39d13730C911b2D286", "DFKSHVAS", "Shvas Rune"),
    ("0x9678518e04Fe02FB30b55e2D0e554E26306d0892", "DFKBLUEEGG", "Blue Pet Egg"),
    ("0x95d02C1Dc58F05A015275eB49E107137D9Ee81Dc", "DFKGREGG", "Grey Pet Egg"),
    ("0x6d605303e9Ac53C59A3Da1ecE36C9660c7A71da5", "DFKGREENEGG", "Green Pet Egg"),
    ("0x9edb3Da18be4B03857f3d39F83e5C6AAD67bc148", "DFKGOLDEGG", "Golden Pet Egg"),
    ("0x3dB1fd0Ad479A46216919758144FD15A21C3e93c", "DFKYELOWEGG", "Yellow Pet Egg"),
    ("0xAC5c49Ff7E813dE1947DC74bbb1720c353079ac9", "DFKBLUESTEM", "Bluestem"),
    ("0xc0214b37FCD01511E6283Af5423CF24C96BB9808", "DFKMILKWEED", "Milkweed"),
    ("0x19B9F05cdE7A61ab7aae5b0ed91aA62FF51CF881", "DFKSPIDRFRT", "Spiderfruit"),
    ("0x17f3B5240C4A71a3BBF379710f6fA66B9b51f224", "DFKGATONECR", "Greater Atonement Crystal"),
    ("0x1f3F655079b70190cb79cE5bc5AE5F19dAf2A6Cf", "DFKLATONECR", "Lesser Atonement Crystal"),
    ("0x27dC6AaaD95580EdF25F8B9676f1B984e09e413d", "DFKATONECR", "Atonement Crystal"),
    ("0x959ba19508827d1ed2333B1b503Bd5ab006C710e", "DFKSTMNPTN", "Stamina Vial"),
    ("0x872dD1595544CE22ad1e0174449C7ECE6F0bb01b", "DFKSWFTPTN", "Swiftness Potion"),
    ("0x2789F04d22a845dC854145d3c289240517f2BcF0", "DFKHLTHPTN", "Health Vial"),
    ("0x87361363A75c9A6303ce813D0B2656c34B68FF52", "DFKFHLTHPTN", "Full Health Potion"),
    ("0xA1f8b0E88c51a45E152934686270DDF4E3356278", "DFKANTPSN", "Anti-poison Potion"),
    ("0xFb03c364969a0bB572Ce62b8Cd616A7DDEb4c09A", "DFKTFNSPTN", "Toughness Potion"),
    ("0x19b020001AB0C12Ffa93e1FDeF90c7C37C8C71ef", "DFKMNPTN", "Mana Vial"),
    ("0xDc2C698aF26Ff935cD1c50Eef3a4A933C62AF18D", "DFKFMNPTN", "Full Mana Potion"),
    ("0x7e120334D9AFFc0982719A4eacC045F78BF41C68", "DFKMGCRSPTN", "Magic Resistance Potion"),
    ("0x1771dEc8D9A29F30d82443dE0a69e7b6824e2F53", "DFKANTBLND", "Anti-blinding Potion"),
    ("0x8F655142104478724bbC72664042EA09EBbF7B38", "DFKMOKSHA", "Moksha Rune"),
    ("0x45B53E55b5c0A10fdd4fE2079a562d5702F3A033", "DFKCHSCR", "Chaos Crystal"),
    ("0xa509c34306AdF6168268A213Cc47D336630bf101", "DFKLCHSCR", "Lesser Chaos Crystal"),
    ("0x3633F956410163A98D58D2D928B38C64A488654e", "DFKCHSST", "Chaos Stone"),
    ("0x6D4f4bC32df561a35C05866051CbE9C92759Da29", "DFKLCHSST", "Lesser Chaos Stone"),
    ("0xc6A58eFc320A7aFDB1cD662eaf6de10Ee17103F2", "DFKFINCR", "Finesse Crystal"),
    ("0x39927A2CEE5580d63A163bc402946C7600300373", "DFKLFINCR", "Lesser Finesse Crystal"),
    ("0xD0B689Cb5DE0c15792Aa456C89D64038C1F2EedC", "DFKFINST", "Finesse Stone"),
    ("0xbb5614D466b77d50DdEd994892DFe6F0ACA4eEbb", "DFKLFINST", "Lesser Finesse Stone"),
    ("0x603919AEB55EB13F9CDE94274fC54ab2Bd2DecE7", "DFKFRTICR", "Fortitude Crystal"),
    ("0x3017609B9A59B77B708D783835B6fF94a3D9E337", "DFKLFRTICR", "Lesser Fortitude Crystal"),
    ("0x17Fa96ba9d9C29e4B96d29A7e89a4E7B240E3343", "DFKFRTIST", "Fortitude Stone"),
    ("0x1f57eb682377f5Ad6276b9315412920BdF9530f6", "DFKLFRTIST", "Lesser Fortitude Stone"),
    ("0x6D777C64f0320d8A5b31BE0FdeB694007Fc3ed45", "DFKFRTUCR", "Fortune Crystal"),
    ("0x13AF184aEA970Fe79E3BB7A1B0B156B195fB1f40", "DFKLFRTUCR", "Lesser Fortune Crystal"),
    ("0x5da2EffE9857DcEcB786E13566Ff37B92e1E6862", "DFKFRTUST", "Fortune Stone"),
    ("0x6D6eA1D2Dc1Df6Eaa2153f212d25Cf92d13Be628", "DFKLFRTUST", "Lesser Fortune Stone"),
    ("0x117E60775584CdfA4f414E22b075F31cC9c3207C", "DFKINSCR", "Insight Crystal"),
    ("0xc63b76f710e9973b8989678eb16234CfADc8D9DB", "DFKLINSCR", "Lesser Insight Crystal"),
    ("0x9D71Bb9C781FC2eBdD3d6cb709438e3c71200149", "DFKINSST", "Insight Stone"),
    ("0x762b98B3758d0A5Eb95B3E4A1E2914Ce0A80D99c", "DFKLINSST", "Lesser Insight Stone"),
    ("0xb368f69bE6eDa74700763672AEB2Ae63f3d20AE6", "DFKMGHTCR", "Might Crystal"),
    ("0xaB464901AFBc61bAC440a97Fa568aC42885Da58B", "DFKLMGHTCR", "Lesser Might Crystal"),
    ("0xE7F6ea1cE7BbEbC9F2Cf080010dd938d2D8D8B1b", "DFKMGHTST", "Might Stone"),
    ("0xe4E7C0c693d8A7FC159776a993495378705464A7", "DFKLMGHTST", "Lesser Might Stone"),
    ("0x5d7f20e3B0f1406Bf038175218eA7e9B4838908c", "DFKSWFTCR", "Swiftness Crystal"),
    ("0xf5c26F2F34E9245C3A9ea0B0e7Ea7B33E6404Da0", "DFKLSWFTCR", "Lesser Swiftness Crystal"),
    ("0x08f362517aD4119d93bBCd20825c2E4119abB495", "DFKSWFTST", "Swiftness Stone"),
    ("0xd9A8abC0Ce1ADC23F1c1813986c9a9C21C9e7510", "DFKLSWFTST", "Lesser Swiftness Stone"),
    ("0xBbA50bD111DC586Fd1f2B1476B6eC505800A3FD0", "DFKVGRCR", "Vigor Crystal"),
    ("0x0d8403E47445DB9E316E36F476dacD5827220Bdd", "DFKLVGRCR", "Lesser Vigor Crystal"),
    ("0x9df75917aC9747B4A70fa033E4b0182d85B62857", "DFKVGRST", "Vigor Stone"),
    ("0xB00CbF5Cd5e7b321436C2D3d8078773522D2F073", "DFKLVGRST", "Lesser Vigor Stone"),
    ("0x3619fc2386FbBC19DDC39d29A72457e758CFAD69", "DFKWITCR", "Wit Crystal"),
    ("0x17ff2016c9ecCFBF4Fc4DA6EF95Fe646D2c9104F", "DFKLWITCR", "Lesser Wit Crystal"),
    ("0x939Ea05C81aAC48F7C10BdB08615082B82C80c63", "DFKWITST", "Wit Stone"),
    ("0x4Ff7A020ec1100D36d5C81F3D4815F2e9C704b59", "DFKLWITST", "Lesser Wit Stone"),
    ("0x0000000000000000000000000000000000000000", "NOTHING", "Nothing")
]

ITEMS_CRYSTALVALE = [
    ("0x04b9dA42306B023f3572e106B11D82aAd9D32EBb", "CRYSTAL", "Crystal"),
    ("0x6e7185872bcdf3f7a6cbbe81356e50daffb002d2", "XCRYSTAL", "xCrystal"),
    ("0x4f60a160D8C2DDdaAfe16FCC57566dB84D674BD6", "JEWEL", "Jewel"),
    ("0x77f2656d04E158f915bC22f07B779D94c1DC47Ff", "XJEWEL", "xJEWEL"),
    ("0x9ed2c155632C042CB8bC20634571fF1CA26f5742", "CJEWEL", "cJEWEL"),
    ("0x576C260513204392F0eC0bc865450872025CB1cA", "DFKGOLD", "DFK Gold"),
    ("0x79fE1fCF16Cc0F7E28b4d7B97387452E3084b6dA", "DFKTEARS", "Gaia's Tears"),
    ("0xB78d5580d6D897DE60E1A942A5C1dc07Bc716943", "DFKAMBRTFY", "Ambertaffy"),
    ("0xA2cef1763e59198025259d76Ce8F9E60d27B17B5", "DFKMILKWEED", "Milkweed"),
    ("0x848Ac8ddC199221Be3dD4e4124c462B806B6C4Fd", "DFKDRKWD", "Darkweed"),
    ("0x0096ffda7A8f8E00e9F8Bbd1cF082c14FA9d642e", "DFKGLDVN", "Goldvein"),
    ("0x3E022D84D397F18743a90155934aBAC421D5FA4C", "DFKSPIDRFRT", "SpiderFruit"),
    ("0x137995beEEec688296B0118131C1052546475fF3", "DFKRGWD", "Ragweed"),
    ("0x473A41e71618dD0709Ba56518256793371427d79", "DFKRDLF", "Redleaf"),
    ("0x60170664b52c035Fcb32CF5c9694b22b47882e5F", "DFKRCKRT", "Rockroot"),
    ("0x0776b936344DE7bd58A4738306a6c76835ce5D3F", "DFKBLUESTEM", "Blue Stem"),
    ("0x97b25DE9F61BBBA2aD51F1b706D4D7C04257f33A", "DFKSWFTHSL", "Swift-Thistle"),
    ("0xe7a1B580942148451E47b92e95aEB8d31B0acA37", "DFKFROSTDRM", "Frost Drum"),
    ("0xBcdD90034eB73e7Aec2598ea9082d381a285f63b", "DFKKNAPROOT", "Knaproot"),
    ("0x80A42Dc2909C0873294c5E359e8DF49cf21c74E4", "DFKSHAGCAP", "Shaggy Caps"),
    ("0xc6030Afa09EDec1fd8e63a1dE10fC00E0146DaF3", "DFKSKNSHADE", "Skunk Shade"),
    ("0x268CC8248FFB72Cd5F3e73A9a20Fa2FF40EfbA61", "DFKBLOATER", "Bloater"),
    ("0x04B43D632F34ba4D4D72B0Dc2DC4B30402e5Cf88", "DFKIRONSCALE", "Ironscale"),
    ("0xc2Ff93228441Ff4DD904c60Ecbc1CfA2886C76eB", "DFKLANTERNEYE", "Lanterneye"),
    ("0x68eE50dD7F1573423EE0Ed9c66Fc1A696f937e81", "DFKREDGILL", "Redgill"),
    ("0x7f46E45f6e0361e7B9304f338404DA85CB94E33D", "DFKSAILFISH", "Sailfish"),
    ("0xd44ee492889C078934662cfeEc790883DCe245f3", "DFKSHIMMERSKIN", "Shimmerskin"),
    ("0xA7CFd21223151700FB82684Cd9c693596267375D", "DFKSILVERFIN", "Silverfin"),
    ("0x3bcb9A3DaB194C6D8D44B424AF383E7Db51C82BD", "DFKFBLOATER", "Frost Bloater"),
    ("0xE7CB27ad646C49dC1671Cb9207176D864922C431", "DFKSPCKLTL", "Speckle Tail"),
    ("0x60A3810a3963f23Fa70591435bbe93BF8786E202", "DFKKINGPNCR", "King Pincer"),
    ("0x6513757978E89e822772c16B60AE033781A29A4F", "DFKTHREEL", "Three Eyed Eel"),
    ("0xa61Bac689AD6867a605633520D70C49e1dCce853", "DFKBLUEEGG", "Blue Pet Egg"),
    ("0x8D2bC53106063A37bb3DDFCa8CfC1D262a9BDCeB", "DFKGREENEGG", "Green Pet Egg"),
    ("0x7E121418cC5080C96d967cf6A033B0E541935097", "DFKGREGG", "Grey Pet Egg"),
    ("0x72F860bF73ffa3FC42B97BbcF43Ae80280CFcdc3", "DFKYELOWEGG", "Yellow Pet Egg"),
    ("0xf2D479DaEdE7F9e270a90615F8b1C52F3C487bC7", "DFKGOLDEGG", "Golden Egg"),
    ("0x242078edFDca25ef2A497C8D9f256Fd641472E5F", "DFKSTMNPTN", "Stamina Vial"),
    ("0x84246Ce3988742D46fC00d9b8b2AFb5CDBDaE660", "DFKSWFTPTN", "Swiftness Potion"),
    ("0x591853e01EcFDcF1Bdc9f093423C197BfBBd1A4f", "DFKHLTHPTN", "Health Vial"),
    ("0x5948dd8Df6afEFE05B033AD8f3ae513a9Cd4F1Dc", "DFKFHLTHPTN", "Full Health Potion"),
    ("0x449eB718e351a86718A090A1a8Db3FD561306d9b", "DFKANTPSN", "Anti-poison Potion"),
    ("0x2dfFf745d2c7ddCAD4E97b80DF33705B1a95A172", "DFKTFNSPTN", "Toughness Potion"),
    ("0x240da5314B05E84392e868aC8f2b80ad6becadd4", "DFKMNPTN", "Mana Vial"),
    ("0xf17FD21bDF6713a1Dfed668b97835b21e32651e8", "DFKFMNPTN", "Full Mana Potion"),
    ("0xFADCb72aAE2713975a890b59FF47231D1A552De3", "DFKMGCRSPTN", "Magic Resistance Potion"),
    ("0x5986045e7c221c8AD40A736B6434D82E29687aeB", "DFKANTBLND", "Anti-blinding Potion"),
    ("0x75E8D8676d774C9429FbB148b30E304b5542aC3d", "DFKSHVAS", "Shvas Rune"),
    ("0xCd2192521BD8e33559b0CA24f3260fE6A26C28e4", "DFKMOKSHA", "Moksha Rune"),
    ("0x3A28E0D4eCF7558e1ba7357070032C5A6105B0C2", "DFKGATONECR", "Greater Atonement Crystal"),
    ("0x1f3F655079b70190cb79cE5bc5AE5F19dAf2A6Cf", "DFKLATONECR", "Lesser Atonement Crystal"),
    ("0xbFa812214a16EcA7814e5F5c270d7f8F37A110B5", "DFKATONECR", "Atonement Crystal"),
    ("0xC6b00B4005883C1Ff09fa1351B0f49027bCAB71a", "DFKCHSCR", "Chaos Crystal"),
    ("0xb0155Fdb7B6972717C4774Fa2AEAEe9D6c0040b9", "DFKGCHSCR", "Greater Chaos Crystal"),
    ("0xeEe5b16Cc49e7cef65391Fe7325cea17f787e245", "DFKLCHSCR", "Lesser Chaos Crystal"),
    ("0x7643ADB5AaF129A424390CB055d6e23231fFd690", "DFKCHSST", "Chaos Stone"),
    ("0x7643ADB5AaF129A424390CB055d6e23231fFd690", "DFKLCHSST", "Lesser Chaos Stone"),
    ("0xA9A8cc1AC7e7505a69cAca2E068716395CebE562", "DFKFINCR", "Finesse Crystal"),
    ("0x9d9ef1Bf6A46b8413bf6b1b54F6A7aAb53c6b1b6", "DFKLFINCR", "Lesser Finesse Crystal"),
    ("0xe2C357ECB698C5ee97c49CCCfA8117c4b943C7B9", "DFKFINST", "Finesse Stone"),
    ("0xF1D53fa23C562246B9d8EC591eEa12Ec0288a888", "DFKLFINST", "Lesser Finesse Stone"),
    ("0xdbEE8C336B06f2d30a6d2bB3817a3Ae0E34f4900", "DFKFRTICR", "Fortitude Crystal"),
    ("0xbd2677c06C9448534A851bdD25dF045872b87cb1", "DFKLFRTICR", "Lesser Fortitude Crystal"),
    ("0x05305c97e9A2FDC0F5Ea23824c1348DEeD9Aff04", "DFKFRTIST", "Fortitude Stone"),
    ("0xf599Ae2c925D3287a7fF64DC1b55C7Ea6EE3AA8f", "DFKLFRTIST", "Lesser Fortitude Stone"),
    ("0xe9BfCc80800EB77a1eAF6881825936770aF83Eb6", "DFKFRTUCR", "Fortune Crystal"),
    ("0xE410b2BE2Ce1508E15009118567d02C6d7A7038e", "DFKLFRTUCR", "Lesser Fortune Crystal"),
    ("0xd647D8b52981eDE13ac6a5B7Ad04e212Ac38fdFb", "DFKFRTUST", "Fortune Stone"),
    ("0x934e3e2a433F37cC2D02855A43fD7Ed475EA7451", "DFKLFRTUST", "Lesser Fortune Stone"),
    ("0x03e56Ded72C3a974295773355EadB38c0A85cF9D", "DFKINSCR", "Insight Crystal"),
    ("0xbb5F97358F60cCBa262883A3Ff0C637393FE3aB8", "DFKLINSCR", "Lesser Insight Crystal"),
    ("0x74CFf096C9B027104fb1a0C2E0e265D123eA47De", "DFKINSST", "Insight Stone"),
    ("0x3D112747ff2463802Afa240B62ade8F1cc4a5c7d", "DFKLINSST", "Lesser Insight Stone"),
    ("0x234dCf10Db6817185F5A3b430a8CAF2B4a35e9E9", "DFKMGHTCR", "Might Crystal"),
    ("0x5bAC3cAd961B01Ef9510C8e6c5402A2bB1542831", "DFKLMGHTCR", "Lesser Might Crystal"),
    ("0x37bAa710391c1D6e22396E4B7F78477F0fF2fFA7", "DFKMGHTST", "Might Stone"),
    ("0xf345b884eA45aEcb3E46CeEaEDB9CE993Ba3615a", "DFKLMGHTST", "Lesser Might Stone"),
    ("0x3e664eB15b35783B9D3EF06702044820F08bB45B", "DFKSWFTCR", "Swiftness Crystal"),
    ("0x6BCA53314dADdA7f4De30A95413f75a93bfAfecF", "DFKLSWFTCR", "Lesser Swiftness Crystal"),
    ("0x4F95D51fB8eF93704aF8C39A080c794cdA08f853", "DFKSWFTST", "Swiftness Stone"),
    ("0xd37aCbAC3C25a543B30aa16208637cfa6EB97eDd", "DFKLSWFTST", "Lesser Swiftness Stone"),
    ("0xcD9201F50e5Be84ECE3D8F603dcd3e9DD5e88ea2", "DFKVGRCR", "Vigor Crystal"),
    ("0x5e4Cf6907CB5fBe2F642E399F6d07E567155d1F8", "DFKLVGRCR", "Lesser Vigor Crystal"),
    ("0xA71a120931526fC98f1AcC9f769b6b0d690fB8f0", "DFKVGRST", "Vigor Stone"),
    ("0x63891e0fcfEe0cEB12dE5fb96F43ADf9DbEC20a3", "DFKLVGRST", "Lesser Vigor Stone"),
    ("0xAeb5b59c8B90D4F078046550Cc8F9f08dC127253", "DFKWITCR", "Wit Crystal"),
    ("0xC989c916F189D2A2BE0322c020942d7c43aEa830", "DFKLWITCR", "Lesser Wit Crystal"),
    ("0x3971212Ec22147EE8808cB84F743DD852Be92f9C", "DFKWITST", "Wit Stone"),
    ("0xFC943eBd19112D6c6098412238E4E8319641B3d8", "DFKLWITST", "Lesser Wit Stone"),
    ("0xAcDa84fAb3d3cdB38078b04901a26c103C37E7F4", "DFKREGTRT", "Regular Pet Treat"),
    ("0x8Df3fFa5a677ba9737CE8Afcb8dd15Bd74085adD", "DFKPRMTRT", "Premium Pet Treat")
]


ITEMS_SERENDALE2 = [
    ("0xB3F5867E277798b50ba7A71C0b24FDcA03045eDF", "JADE", "Jade"),
    ("0x30c103f8f5a3a732dfe2dce1cc9446f545527b43", "JEWEL", "Jewel"),
    ("0xaA8548665bCC12C202d5d0C700093123F2463EA6", "SJEWEL", "sJEWEL"),
    ("0xe7a1B580942148451E47b92e95aEB8d31B0acA37", "DFKGOLD", "DFK Gold"),
    ("0x8Be0cbA3c8c8F392408364ef21dfCF714A918234", "DFKTEARS", "Gaia's Tears"),
    ("0x75E8D8676d774C9429FbB148b30E304b5542aC3d", "DFKAMBRTFY", "Ambertaffy"),
    ("0xDbd4fA2D2C62C6c60957a126970e412Ed6AC1bD6", "DFKBLUESTEM", "Bluestem"),
    ("0xEDFBe9EEf42FfAf8909EC9Ce0d79850BA0C232FE", "DFKDRKWD", "Darkweed"),
    ("0xeaF833A0Ae97897f6F69a728C9c17916296cecCA", "DFKGLDVN", "Goldvein"),
    ("0xBcdD90034eB73e7Aec2598ea9082d381a285f63b", "DFKIRONSCALE", "Ironscale"),
    ("0x80A42Dc2909C0873294c5E359e8DF49cf21c74E4", "DFKLANTERNEYE", "Lanterneye"),
    ("0xE408814828f2b51649473c1a05B861495516B920", "DFKMILKWEED", "Milkweed"),
    ("0xf2D479DaEdE7F9e270a90615F8b1C52F3C487bC7", "DFKRCKRT", "Rockroot"),
    ("0xc6030Afa09EDec1fd8e63a1dE10fC00E0146DaF3", "DFKSAILFISH", "Sailfish"),
    ("0xa61Bac689AD6867a605633520D70C49e1dCce853", "DFKSHIMMERSKIN", "Shimmerskin"),
    ("0x874FC0015ece1d77ba3D5668F16c46ba72913239", "DFKSKNSHADE", "Skunk Shade"),
    ("0x08D93Db24B783F8eBb68D7604bF358F5027330A6", "DFKSPIDRFRT", "Spiderfruit"),
    ("0xCd2192521BD8e33559b0CA24f3260fE6A26C28e4", "DFKSWFTHSL", "Swift-Thistle"),
    ("0x7E1298EBF3a8B259561df6E797Ff8561756E50EA", "DFKTHREEL", "Three-Eyed Eel"),
    ("0x72F860bF73ffa3FC42B97BbcF43Ae80280CFcdc3", "DFKBLOATER", "Bloater"),
    ("0x18cB286EeCE992f79f601E49acde1D1F5dE32a30", "DFKFBLOATER", "Frost Bloater"),
    ("0xD69542aBE74413242e387Efb9e55BE6A4863ca10", "DFKFROSTDRM", "Frost Drum"),
    ("0xB4A516bf36e44c0CE9E3E6769D3BA87341Cd9959", "DFKKINGPNCR", "King Pincer"),
    ("0xFceFA4Abcb18a7053393526f75Ad33fac5F25dc9", "DFKKNAPROOT", "Knaproot"),
    ("0x4cD7025BD6e1b77105b90928362e6715101d0b5a", "DFKRGWD", "Ragweed"),
    ("0x8D2bC53106063A37bb3DDFCa8CfC1D262a9BDCeB", "DFDFDFDF", "Redgill"),
    ("0xadbF23Fe3B47857614940dF31B28179685aE9B0c", "DFKRDLF", "Redleaf"),
    ("0xCe370D379f0CCf746B3426E3BD3923f3aDF0DC1a", "DFKSHAGCAP", "Shaggy Caps"),
    ("0x7E121418cC5080C96d967cf6A033B0E541935097", "DFKSILVERFIN", "Silverfin"),
    ("0x48d9fC80A47cee2d52DE950898Bc6aBF54223F81", "DFKSPCKLTL", "Speckle Tail"),
    ("0x29ADd7D022c591D56eb4aFd262075dA900C67ab1", "DFKBLUEEGG", "Blue Pet Egg"),
    ("0xb1Ec534fBBfEBd4563A4B0055E744286CE490f26", "DFKGREENEGG", "Green Pet Egg"),
    ("0xfd29ebdE0dd1331C19BBF54518df94b442ACb38C", "DFKGREGG", "Grey Pet Egg"),
    ("0x0A73aF98781bad9BCb80A71241F129EA877eF1b7", "DFKYELOWEGG", "Yellow Pet Egg"),
    ("0xc9731BE04F217543E3010cCbf903E858EFde840f", "DFKGOLDEGG", "Golden Egg"),
    ("0x5FB537aF1d929af7BDD7935C289158c940782ed6", "DFKANTBLND", "Anti-blinding Potion"),
    ("0xE34a733fA92B41A1CA4241da9D2d5834Cc8D1011", "DFKANTPSN", "Anti-poison Potion"),
    ("0xf710244462431b9962706B46826AFB3B38376c7b", "DFKFHLTHPTN", "Full Health Potion"),
    ("0x108D31E23bC6540878E6532F3376b3EC982e1C58", "DFKFMNPTN", "Full Mana Potion"),
    ("0xa27C1429a676db902B9f0360686eDbB57d0A7B01", "DFKHLTHPTN", "Health Vial"),
    ("0x9c8A0C6a7ad8Be153773070D434CDbeA5176D2ff", "DFKMGCRSPTN", "Magic Resistance Potion"),
    ("0x8639d64A2088500EC4f20fB5C41A995fE4f1d85a", "DFKMNPTN", "Mana Vial"),
    ("0x4546DBaAb48Bf1BF2ad7B56d04952d946Ab6e2a7", "DFKSTMNPTN", "Stamina Vial"),
    ("0xcb7aA7cA9357DAF9F2b78D262A4f89cDfE5abC70", "DFKSWFTPTN", "Swiftness Potion"),
    ("0xf757a7F4ffF29e7F7b4aCCe6Ffb04E59e91EFDA8", "DFKTFNSPTN", "Toughness Potion"),
    ("0x907a98319AEB249e387246637149f4B2e7D21dB7", "DFKSHVAS", "Shvas Rune"),
    ("0xd0223143057Eb44065e789b202E03A5869a6006C", "DFKMOKSHA", "Moksha Rune"),
    ("0xE078C782fF0cC1789D0608834A3cD5076896e4FC", "DFKCHSCR", "Chaos Crystal"),
    ("0x537E800b8fD22Dc76A438Af8b9923986A5487853", "DFKLCHSCR", "Lesser Chaos Crystal"),
    ("0x880cb941AAb394775f54F2b6468035bbdD0B81dF", "DFKCHSST", "Chaos Stone"),
    ("0x38bDed7C399bbD214a19De35260766b130cAFd2F", "DFKLCHSST", "Lesser Chaos Stone"),
    ("0x15E77beB33D3B09aB7da529daB1E556b955fECf6", "DFKFINCR", "Finesse Crystal"),
    ("0xC3B36a02f360c3d18042bF3533be602cb775007A", "DFKLFINCR", "Lesser Finesse Crystal"),
    ("0x31eb3b534E29D10Db08109A1fa50ccB081d10816", "DFKFINST", "Finesse Stone"),
    ("0x784bd01e3882b80aa837f6A3041Cd386eC54a501", "DFKLFINST", "Lesser Finesse Stone"),
    ("0xA844059503289B781854aEdcA04E5bB13290bd86", "DFKFRTICR", "Fortitude Crystal"),
    ("0x1E672a8385b39E13267efA2Fb39f574a2a23AE9F", "DFKLFRTICR", "Lesser Fortitude Crystal"),
    ("0x254787d3b87d8c21A300Ab8D5A06C01426CE40c0", "DFKFRTIST", "Fortitude Stone"),
    ("0xBC5248B4f50f4c7D2F9A67Be1f1d4b8be44ffc75", "DFKLFRTIST", "Lesser Fortitude Stone"),
    ("0x02d27BC195E58498C687A82d96188A8EF282a1e1", "DFKFRTUCR", "Fortune Crystal"),
    ("0x8baD15B5C531d119b328d0F716a6B9D90CeDa88A", "DFKLFRTUCR", "Lesser Fortune Crystal"),
    ("0xf0cBbd41652d9A93A899f070669186F0c8475F7D", "DFKFRTUST", "Fortune Stone"),
    ("0x816E22125021530535364390a3E2fA305a436247", "DFKLFRTUST", "Lesser Fortune Stone"),
    ("0xAd7fBD9EDDE05227964104Bb23Ff8d171D4c90C8", "DFKINSCR", "Insight Crystal"),
    ("0x5f967E325E91977B42D2591Fc2f57da75Ee4490B", "DFKLINSCR", "Lesser Insight Crystal"),
    ("0x22A92428605a3B5b66695A60e96b683E98a9a035", "DFKINSST", "Insight Stone"),
    ("0xfC66cF68505F8E95C52C4F7f84936436DBd52e9B", "DFKLINSST", "Lesser Insight Stone"),
    ("0xa3907dEA6f16f1918B4BcDd178c2928c7e6A571D", "DFKMGHTCR", "Might Crystal"),
    ("0x80Ab38fc9fA0a484b98d5600147e7C695627747D", "DFKLMGHTCR", "Lesser Might Crystal"),
    ("0x532bce28c28616552a4BcDdb5D4B4126Dea35f66", "DFKMGHTST", "Might Stone"),
    ("0xbb8ac0BB95E433204217b0478B3f6d815EcB2d8C", "DFKLMGHTST", "Lesser Might Stone"),
    ("0xc2Ff16F357b51E070c977501563A01a70F3B7BF5", "DFKSWFTCR", "Swiftness Crystal"),
    ("0x32Cbbfd741EB7634818aa2e3E8502367cB6602BE", "DFKLSWFTCR", "Lesser Swiftness Crystal"),
    ("0xf200597430eAc3e22B4566D1BCd70A3b63804B24", "DFKSWFTST", "Swiftness Stone"),
    ("0xAd51199B453075C73FA106aFcAAD59f705EF7872", "DFKLSWFTST", "Lesser Swiftness Stone"),
    ("0x14a9D5a75799E4C6B4BfA65C8293a75e02DD5339", "DFKVGRCR", "Vigor Crystal"),
    ("0x6C7AF7483b050a00b5fbC4241eD06944c5f0bD77", "DFKLVGRCR", "Lesser Vigor Crystal"),
    ("0xA0c89fB3cbb115cf86EdcB4319578312D026A07a", "DFKVGRST", "Vigor Stone"),
    ("0x50F683acefA41b226CEfAdc0dd2ea6fFBfED56A0", "DFKLVGRST", "Lesser Vigor Stone"),
    ("0xf30214D43E55BE1cbaC712b49A75d4D3220302a7", "DFKWITCR", "Wit Crystal"),
    ("0xf15035b5eD13Feb18f63D829ABc1c3139041e7C2", "DFKLWITCR", "Lesser Wit Crystal"),
    ("0x3BaEFAfF21Fa2F06Ad3899903B7A899a91B5915A", "DFKWITST", "Wit Stone"),
    ("0x5903F478e456DD4Ce5387caBE3984DfEf93D0A46", "DFKLWITST", "Lesser Wit Stone"),
    ("0x2F11e335224C5aBd3418B99922A9fe442F5696E9", "DFKREGTRT", "Regular Pet Treat"),
    ("0xEec86C39e061B3Dec44f608Ff0ADA8053B8fFaDb", "DFKPRMTRT", "Premium Pet Treat")
]

ABI = """
        [
            {"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},
            {"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"MINTER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"PAUSER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burnFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"}
        ]
        """


def wei2eth(w3, wei):
    return w3.from_wei(wei, 'ether')


def eth2wei(w3, eth):
    return w3.to_wei(eth, 'ether')


def block_explorer_link(token_address, txid):
        return str(txid)


def get_realm_item_list(realm):
    realm = realm.lower().strip()
    if realm in SERENDALE_IDS:
        return ITEMS_SERENDALE
    elif realm in CRYSTALVALE_IDS:
        return ITEMS_CRYSTALVALE
    elif realm in SERENDALE2_IDS:
        return ITEMS_SERENDALE2
    else:
        return None


def symbol2item(_symbol, realm):
    _symbol = _symbol.upper().strip()
    items = get_realm_item_list(realm)

    for item in items:
        if item[1] == _symbol:
            return item
    return None


def symbol2address(_symbol, realm):
    _symbol = _symbol.upper().strip()
    items = get_realm_item_list(realm)

    for item in items:
        if item[1] == _symbol:
            return item[0]
    return None


def address2item(address, realm):
    address = address.upper().strip()
    items = get_realm_item_list(realm)

    for item in items:
        if item[0].upper() == address:
            return item
    return None


def address2symbol(address, realm):
    address = address.upper().strip()
    items = get_realm_item_list(realm)

    for item in items:
        if item[0].upper() == address:
            return item[1]
    return None


def all_items(realm):
    items = get_realm_item_list(realm)
    return items.copy()


def symbol(token_address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(token_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.symbol().call()


def name(token_address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(token_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.name().call()


def decimals(token_address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(token_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.decimals().call()


def balance_of(address, token_address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.to_checksum_address(token_address)
    contract = w3.eth.contract(contract_address, abi=ABI)
    result = contract.functions.balanceOf(address).call()

    return result


def approve(token_address, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.from_key(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.to_checksum_address(token_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.approve(account.address, sys.maxsize)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.build_transaction(
            {'maxFeePerGas': w3.to_wei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.to_wei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.build_transaction({'gasPrice': w3.to_wei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    
    logger.info("Waiting for transaction " + block_explorer_link(token_address, signed_tx.hash.hex()) + " to be mined")
    
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def transfer(token_address, private_key, nonce, dest_address, amount, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.from_key(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.to_checksum_address(token_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.transferFrom(account.address, dest_address, amount)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.build_transaction(
            {'maxFeePerGas': w3.to_wei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.to_wei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.build_transaction({'gasPrice': w3.to_wei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    
    logger.info("Waiting for transaction " + block_explorer_link(token_address, signed_tx.hash.hex()) + " to be mined")
    
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt
