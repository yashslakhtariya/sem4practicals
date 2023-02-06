import "/validate.js"
import "/rating.js"
import "/payment.js"
import { validateInfo } from "./validate";
import { prcsPymnt } from "./payment";
import { calculateRating } from "./rating";

function createAc()
{
     validateInfo("haribol","harekrsna","YSL64");
     prcsPymnt(6400, 16);
     calculateRating();
}