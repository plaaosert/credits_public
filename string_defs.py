# Contains strings used inside credits.py.
# Kept inside this file to reduce clutter.
# Implemented as a dictionary of in-memory strings.
from animation_functions import split_word_template, fuck_up_text, work_out_date

data_strings = {}

data_strings["ocean_b_0"] = (
    "Now for the official national~ weather~ service~ forecast\n"
    "~~~~for~~ Eastern Massachusetts~ inside of~~ I-~~~~4~~~~9~~~~~~~5~~,\n"
    "~~~~~~~~    including Boston,\n\n"
    "~~~~~~~~issued at 7~~~~:2~~1~~~~ PM~~~~, ~~~~~~~~~~~~~~Thursday, October~~ 2~~2~~nd."
)

data_strings["ocean_b_1"] = (
    "Tonight:\n\n~~~~~Mostly cloudy with isolated~ showers~ until~~ mid~~~~night,\n"
    "~~~~~~~~~then mostly clear~~ after~~ mid~night.\n"
    "~~~~~~~~~Lows in the lower 4~~~~0~~~~s.\n"
    "~~~~~~~~~West winds 10~ to~~ 1~~5~~ miles~~ an~~ hour\n"
    "~~~~~with~ gusts~~ up~ to~ 2~~~~5~~~~ miles~~ an~~ hour~~.\n"
    "~~~~~~~~~~Chance of rain:~~~~ 2~~0~~~~ per~cent."
)

data_strings["ocean_b_2"] = (
    "Friday:\n\n~~Sunny.\n~~~~~~~~~~~~~~~~Lush colour with highs in the low~er 5~~~0~s.\n"
    "~~~~~~~~~~Northwest~~ winds~~ 10~~-~1~~5~~ miles~~ an~~ hour\n"
    "~~~~with gusts up to~~ 2~~~~5~~~~ miles~~ an~~ hour~~.\n"
    "~~~~~~~~~~~~~~~~Friday night,~~ mostly~ clear.\n"
    "~~~~~~~~~~~~~~Lows in the mid-3~~~~0~~s.\n"
    "~~~~~~~~~~~~~~~~North winds 10-1~~~5~~ miles~~ an~~ hour~~."
)

data_strings["ocean_b_3"] = (
    "Saturday:\n\n~~~~~~~~Partly sunny.\n"
    "~~~~~~~~High-@igh-@igh-@igh-@igh-@igh-@igh-@igh-@igh-@igh-@igh-@igh-@igh-@igh-@igh-@igh-@igh-@igh-@igh-i"
)

data_strings["ocean_c_0"] = (
    "Here~ are~ the 7~~~~ P~~~~M~~~~ ob~ser~va~tions for~~ the\n"
    "~~~Bos~ton~~ metro~po~li~tan~~~ ar~ea.\n\n"
    "~~~~~~~~~~~~~~~At Logan~~~~ Airport,~~~~~~ it was clou~~~~dy.\n"
    "~~~~~~~~~~~~~~~The tem~per~a~ture was 6~~~~8~~~~ de~grees,\n"
    "~~~~~~~~the dew point,~~ 4~~~~7~~ -\n"
    "~~~~~~and~ the~ re~la~tive~~ hu~mi~di~ty,~~~~ 4~~~~6~~~~ per~~cent.\n"
    "~~~~~~~~~~~~~~~~The~ wind~ was~ south~~west~ at 1~~~~3~ miles~~~~ an~~~~ ho~ur.\n"
    "~~~~~~~~~~~~The~ pres~~sure~~ was~~ 2~~~~9~~~~.~~~~~~~~9~~~~~~9~~~~~~ in~ches and ri~sing.\n"
    "~~~~~~~~Elsewher" + fuck_up_text(
        "rrrrrrrrr\n", 800
    )
)

data_strings["ocean_c_1"] = (
    fuck_up_text(
        "Here~ are~ the 7~~~~ P~~~~M~~~~ ob~ser~va~tions for~~ the\n"
        "~~~Bos~ton~~ metro~po~li~tan~~~ ar~ea.\n\n"
        "~~~~~~~~~~~~~~~At Logan~~~~ Airport,~~~~~~ it was clou~~~~dy.\n"
        "~~~~~~~~~~~~~~~The tem~per~a~ture was 6~~~~8~~~~ de~grees,\n"
        "~~~~~~~~the dew point,~~ 4~~~~7~~ -\n"
        "~~~~~~and~ the~ re~la~tive~~ hu~mi~di~ty,~~~~ 4~~~~6~~~~ per~~cent.\n"
        "~~~~~~~~~~~~~~~~The~ wind~ was~ south~~west~ at 1~~~~3~ miles~~~~ an~~~~ ho~ur.\n"
        "~~~~~~~~~~~~The~ pres~~sure~~ was~~ 2~~~~9~~~~.~~~~~~~~9~~~~~~9~~~~~~ in~ches and ri~sing.\n"
        "~~~~~~~~Elsewher", 100
    ) + fuck_up_text(
        "rrrrrrrrr\n", 900
    )
)

data_strings["ocean_c_2"] = (
    fuck_up_text(
        "Here~ are~ the 7~~~~ P~~~~M~~~~ ob~ser~va~tions for~~ the\n"
        "~~~Bos~ton~~ metro~po~li~tan~~~ ar~ea.\n\n"
        "~~~~~~~~~~~~~~~At Logan~~~~ Airport,~~~~~~ it was clou~~~~dy.\n"
        "~~~~~~~~~~~~~~~The tem~per~a~ture was 6~~~~8~~~~ de~grees,\n"
        "~~~~~~~~the dew point,~~ 4~~~~7~~ -\n"
        "~~~~~~and~ the~ re~la~tive~~ hu~mi~di~ty,~~~~ 4~~~~6~~~~ per~~cent.\n"
        "~~~~~~~~~~~~~~~~The~ wind~ was~ south~~west~ at 1~~~~3~ miles~~~~ an~~~~ ho~ur.\n"
        "~~~~~~~~~~~~The~ pres~~sure~~ was~~ 2~~~~9~~~~.~~~~~~~~9~~~~~~9~~~~~~ in~ches and ri~sing.\n"
        "~~~~~~~~Elsewher", 200
    ) + fuck_up_text(
        "rrrrrrrrr\n", 1000
    )
)

data_strings["ocean_c_3"] = (
    fuck_up_text(
        "Here~ are~ the 7~~~~ P~~~~M~~~~ ob~ser~va~tions for~~ the\n"
        "~~~Bos~ton~~ metro~po~li~tan~~~ ar~ea.\n\n"
        "~~~~~~~~~~~~~~~At Logan~~~~ Airport,~~~~~~ it was clou~~~~dy.\n"
        "~~~~~~~~~~~~~~~The tem~per~a~ture was 6~~~~8~~~~ de~grees,\n"
        "~~~~~~~~the dew point,~~ 4~~~~7~~ -\n"
        "~~~~~~and~ the~ re~la~tive~~ hu~mi~di~ty,~~~~ 4~~~~6~~~~ per~~cent.\n"
        "~~~~~~~~~~~~~~~~The~ wind~ was~ south~~west~ at 1~~~~3~ miles~~~~ an~~~~ ho~ur.\n"
        "~~~~~~~~~~~~The~ pres~~sure~~ was~~ 2~~~~9~~~~.~~~~~~~~9~~~~~~9~~~~~~ in~ches and ri~sing.\n"
        "~~~~~~~~Elsewher", 250
    ) + fuck_up_text(
        "rrrrrrrrr\n", 1000
    )
)

data_strings["funding_0"] = (
    split_word_template(
        "Fun####ding#### for#### this#### pro####gram#### was#### made#### pos####si####ble###~\n"
        "  by###\n"
        "    by###\n"
        "      by###\n"
        "        by###\n"
        "          by#\n"
        "Fun#\n"
        "   by\n"
        "     by\n"
        "       by\n"
        "         by\n"
        "Funding#\n"
        "       by\n"
        "         by\n"
        "           by\n"
        "             by\n"
        "Funding for\n"
        "Funding for thi#i#i#i#i#\n"
        "Funding for this pro####gram###\n"
        "Funding for this pro####gram###\n"
        "                   pro\n"
        "                     pro\n"
        "                       pro\n"
        "Funding for this pro#gram.#~\n"
        "Fun####ding#### for#\n"
        "           by#\n"
        "             by#\n"
        "Funding made#### pos####si####ble#### by#### view####ers#### like#### you.###~\n"
        "####like#### you.##\n"
        "####like#### you.##\n"
        "####like#### you.##\n"
        "####like#### you.##\n"
        "####like#### you.##\n"
        "####like#### you.\n"
        " Fu\n"
        "  Fu\n"
    ) * 2
)

data_strings["funding_1"] = (
    split_word_template(
        "Broad####cast####\n"
        "Broadcast Cor####por##a####tion.~#####\n"
        "Cor####po##ra####tion.#####\n"
        "Cor####po##ra####tion.#####\n"
        " Cor###po\n"
        "  Cor###po\n"
        "    Co\n"
        "      Co\n"
        "Cor####po##ra####tion.#####\n"
        "Cor####po##ra####tion.#####\n"
        "Cor####po##ra####tion.#####\n"
        " Cor###po\n"
        "  Cor###po\n"
        "    Co\n"
        "      Co\n"
        "Cor####po##ra###tion.#\n"
        " Co\n"
        "  Co\n"
        "Cor####po##ra###tion.#\n"
        " Co\n"
        "  Co\n"
        "Cor####po##ra###tion.#\n"
        " Co\n"
        "  Co\n"
        "Cor####po##ra###tion.#\n"
        " Co\n"
        "  Co\n"
        "Cor####po##ra###tion.#\n"
        " Co\n"
        "  Co\n"
        "Cor####po##ra###tion.#\n"
        " Co\n"
        "  Co\n"
        " Cor###po\n"
        "  Cor###po\n"
        "    Cor###po\n"
        "      Cor###po\n"
        "...#######\n"
        " Cor###po#\n"
        "     cor##\n"
        "  cor###po#\n"
        "    cor###po#\n"
        " cor##\n"
        "      cor###po#\n"
        "  cor###po#\n"
        "         cor##\n"
        "     cor###po#\n"
        " cor##\n"
        "   cor##\n"
        "     cor##\n"
        "       co#\n"
        "     co#\n"
        " cor###po#\n"
        "   cor##\n"
        " cor###po#\n"
        "   cor###po#\n"
        "     cor##\n"
        "       cor##\n"
        "         cor###po#\n" + fuck_up_text(

            " cor###po#\n"
            "   cor#\n"
            " cor###po#\n"
            "   cor#\n"
            "     cor#\n", 100, "# "
        ) + " ...#\n" + fuck_up_text(

            " co#\n"
            "  co#\n"
            " cor###po#\n"
            "   cor##\n"
            "     cor###po#\n"
            "   cor###po#\n"
            "            cor##\n"
            "      cor###po#\n", 280, "# "
        ) + fuck_up_text(

            "             cor###po#\n"
            "    cor##\n"
            "                  cor###po#\n"
            "  cor#\n"
            "          cor#\n"
            "                    cor#\n", 500, "# "
        ) + fuck_up_text(

            " co#\n"
            "                co#\n"
            "     cor###po#\n"
            "                        cor#\n"
            "  cor###po#\n"
            "           cor###po#\n"
            "             cor#\n"
            "  cor###po#\n", 650, "# "
        ) +

        " ???###p?#\n"
        "   ??r#\n"
        "           ???###??#\n"
        "                       co?#\n"
        "                                       ???#\n"
    
        "....#....#....#....#....#....#....#....#...#...#...#...#..#..\n"
        "              <##C##O##N##N##E##C##T##I##O##N## ##L##O##S##T##>"
        "##########################################################################################################"
        "##########################################################################################################"
        "##########################################################################################################"
        "##########################################################################################################"
    )
)

data_strings["funding_2"] = (
    split_word_template(
        "--####--####-- ####-i####-a-####---- ####-up####-o-#\n" +
        "-n####nu####-l ####fi####nan####cial ####sup####por#\n" +
        "An####nu####al ####fi####nan####cial ####sup####por#\n" * 5 +
        "An####nu###\nAn####nu###\n"
    )
)

data_strings["fundingx2_0"] = (
    split_word_template(
        " By\n"
        "  ci\n"
        "    po\n"
        "      po\n"
        "  cor#\n"
        "    cor#\n"
        "        by#\n"
        "          by#\n"
        "rr#rr#rr#ro#oo#oo#aa#aa#aa#\n##"
        "  wers#\n"
        " ble#\n"
        "       b\n"
        "         b\n"
        "           F#\n"
        "         f\n"
        "       fi\n"
        "     i\n"
        "na#aa#aa#aa#aa#aa#aa#aa#\n"
        " Fun\n"
        "Fun####ding#\n"
        " Fu#\n"
        "  Fun#\n"
        " fu#\n"
        "Fun####ding#\n"
        " Fu#\n"
        "  Fun#\n"
        " fu#\n"
        "Fun####ding#\n"
        " Fu#\n"
        "  Fun#\n"
        " fu#\n"
        "Fun####ding#\n"
        "F\n"
        "    Fi\n"
        "   Fin\n"
        "          Fina\n"
        "      Finan\n"
        "po\n"
        "po\n"
        "cor#\n"
        "by#\n"
        "  por\n"
        "Por#tio##\n"
        "Por#tio##\n"
        "Por#tion# nn#nn#nn\n"
        "b\n"
        " b\n"
        "by###\n"
        "---- by###\n"
        "-------- by###\n"
        "------------ by###\n"
        "---------------- by#######\n"
        ">>#>>###\n"
        "By#\n"
        "  by#\n"
        "fi#nan#\n"
        " b#\n"
        "  b#\n"
        "   nc#\n"
        "    nc#\n"
        "Corr#rr#rr#\n"
        "View####ers#### like#### you.#\n"
        "      like#### you.#\n"
        "    like## you.#\n"
        "Fun####ding###\n"
        "Fun####ding###\n"
        "  Fun###\n"
        "    Fu#\n"
        "Fun####ding###\n"
        "  fu#\n"
        "    fu#\n"
        "      fu#\n"
        "        fu#\n"
        "          fu#\n"
        "Cor####por####a####tion\n"
        "The#### cor####por####a####tion#### for#### pub####lic####"
        " broad####cast####ing#### and#### bi####-an####nual#### fii#ii#i\n"
        "of#\n"
        "nan#\n"
        "for#\n"
        "fin####an####cial#### su#\n"
        "for#### fin####an####cial#### ass#ss#ss\n"
        "in#\n"
        "view####ers###\n"
        "you#####\n"
        "| ########This######## is######## P####B####S!############~\n"
    )
)

data_strings["fundingx2_1"] = (
    split_word_template("\n".join(
        "{}#### Unknown###".format(
            work_out_date((64 * 3390) + i * 64)).replace(".", ".####") for i in range(26)
    ) + "\n| ########This######## is######## P####B####S!############~\n")
)

data_strings["fundingx2_2"] = (
    split_word_template(
        "S#e#a#r#c#h#i#n#g# #f#o#r# #a#c#c#e#s##s## ##p##o##i##n##t"
        "########.########.########.########\n" +
        "Searching for access point########.########.########.########\n" * 11 +
        "Found:################"
        " P#B#S# #O#f#f#i#c#i#a#l# #1#1#.#### #R#e#s#t#a#r#t#i#n#g#.####.####.####"
    )
)

data_strings["fdg_single_0"] = (
    split_word_template(
        "########.########.########.########.########.########.########.#######\n"
        "########.########.########.########.########.########.########.#######\n"
        "########.########.########.########.########.########.########.#######\n"
        "########.########.########.########.########.########.########.#######\n"
        "########.########.########.########.########.########.########.#######\n"
        "########.########.########.########.########.########.########.#######\n"
        "Fun####ding#### for#### this#### pro####gram#### was#### made#### pos####sible#\n"
        " 7 > > > by###\n"
        " 7 > > > > by###\n"
        " 8 > > > by###\n"
        " 8 > > > > by###\n"
        " 9 > > > by###\n"
        "Fun##\n"
        "     by\n"
        "       by\n"
        "         by\n"
        "           by\n"
        "Funding#\n"
        "     by\n"
        "       by\n"
        "         by\n"
        "           by\n"
        "for\n"
        "thi#i#i#i\n"
        "Pro####gram.#\n"
        "Pro####gram.#\n"
        "Pro\n"
        "  pro\n"
        "    pro\n"
        "      pro\n"
        "Pro####gram.###\n"
        "Fun####ding#### for####\n"
        "            by#\n"
        "              by#\n"
        "Funding for made#### pos####sible#### by#### view####ers#### like#### you.###\n"
        "like#### you.#####\n"
        "##like#### you.#####\n"
        "##like#### you.#####\n"
        "##like#### you.#####\n"
        "##like#### you.#####\n"
        "##like#### you.###\n"
        "Fu\n"
        "  Fu\n"
        "Fun####ding#### for#### this#### pro####gram#### was#### made#### pos####sible#### by#\n"
        "                                         by###\n"
        "                                       by###\n"
        "                                     by###\n"
        "                                   by#\n"
        "Fun###\n"
        "     by\n"
        "       by\n"
        "         by\n"
        "           by\n"
        "Funding#\n"
        "     by\n"
        "       by\n"
        "         by\n"
        "           by\n"
        "for\n"
        "thi#i#i#i\n"
        "Pro####gram.###\n"
        "Pro####gram.###\n"
        "Pro\n"
        "  pro\n"
        "    pro\n"
        "      pro\n"
        "Pro####gram.#\n"
        "Fun####ding#### for####\n"
        "            by#\n"
        "              by#\n"
        "Funding for made#### pos####sible#### by#### view####ers#### like#### you.###\n"
        "like#### you.#####\n"
        "##like#### you.#####\n"
        "##like#### you.#####\n"
        "##like#### you.#####\n"
        "##like#### you.#####\n"
        "####< RET 200################################################################\n"
    )
)

data_strings["fdg_down_0"] = (
    split_word_template(
        "Fun####ding#### for#### this#### pro####gram#### was#\n"
        "made#### made#### made#### made#### made#### made#### made#### made#### made###\n"
        "pos####sible#### by#### view####ers#### like#### you.#######"
    )
)

data_strings["fdg_down_1"] = (
    split_word_template(
        "---####----#### ---#### ----#### ---####----#### ---#\n"
        "----#### ----#### ----#### ----#### ----#### ----#### ----#### ----#### ----###\n"
        "---####-----#### --#### ----####---###### ----######## -##-##-##.#######"
    )
)

data_strings["fdg_down_2"] = (
    split_word_template(
        "Fun####ding#### for#### this#### pro####gram#### was#\n"
        "made#### made#### made#### made#### made#### made#### made#### made#### made###\n"
        "pos####sible#### by#### view####ers###### like######## y##o##u##.#######"
    )
)
