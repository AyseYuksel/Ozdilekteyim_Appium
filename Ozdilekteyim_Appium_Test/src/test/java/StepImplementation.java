
import com.thoughtworks.gauge.Step;
import io.appium.java_client.android.AndroidTouchAction;
import io.appium.java_client.touch.offset.PointOption;
import org.openqa.selenium.By;
import org.apache.log4j.Logger;

public class StepImplementation extends BaseTest {

    public Logger logger = Logger.getLogger(getClass());

    @Step("<time> saniye bekle")
    public void waitTime(int time) throws InterruptedException {
        Thread.sleep(1000* time);
        logger.info(time+"saniye beklendi");
    }

    @Step("<key> id'li elementine tıkla")
    public void clickElementByid(String key){
        appiumDriver.findElement(By.id(key)).click();
        logger.info(key+"elementine tiklandi.");
    }

    @Step("<Key> İd'li elemente <keyword> değerini yaz")
    public void SendkeyElementByid(String Key,String keyword){
       appiumDriver.findElement(By.id(Key)).sendKeys(keyword);
        logger.info(Key+"alanina"+keyword+"yazildi");

    }

    @Step("<Key> xpath'li elemente tıkla")
    public void clickElementByxpath(String Key){
        appiumDriver.findElement(By.xpath(Key)).click();
        logger.info(Key+"alanına tıklandı");
    }
    @Step("<Key> xpath'li elemente <keyword> değerini yaz")
    public void SendkeyElementByxpath(String Key,String keyword){
        appiumDriver.findElement(By.xpath(Key)).sendKeys(keyword);
        logger.info(Key+"alanina"+keyword+"yazildi");

    }

    @Step("<Key> id'li element sayfada var mı doğru sayfada mıyım kontrolü yap")
    public boolean isDisplayed(String Key){
       boolean a= appiumDriver.findElement(By.id(Key)).isDisplayed();
        if(a){
            logger.info("Element bulundu.Doğru sayfadasınız");
       }else{
            logger.info("Element bulunamadı.Yanlış sayfadasınız.");
        }
        return appiumDriver.findElement(By.id(Key)).isDisplayed();

    }

    @Step("<Key> xpath'ine sahip element sayfada var mı, doğru sayfada mıyım kontrolü yap")
    public boolean isDisplayedxpath(String Key){
        boolean a= appiumDriver.findElement(By.id(Key)).isDisplayed();
        if(a){
            logger.info("Element bulundu.Doğru sayfadasınız");
        }else{
            logger.info("Element bulunamadı.Yanlış sayfadasınız.");
        }
        return appiumDriver.findElement(By.xpath(Key)).isDisplayed();
    }

    @Step("Sayfayı asagi indir")
    public void scrollFeature() {
        (new AndroidTouchAction(appiumDriver)).press(new PointOption().withCoordinates(540, 1450))
                .moveTo(new PointOption().withCoordinates(525, 675))
                .release().perform();
        logger.info("sayfa asagı indirildi");
    }

    @Step("ürün sayfasını asagi indir")
    public void scrollFeatureProduct() {
        (new AndroidTouchAction(appiumDriver)).press(new PointOption().withCoordinates(740, 1387))
                .moveTo(new PointOption().withCoordinates(730, 813))
                .release().perform();
        logger.info("sayfa asagı indirildi");
    }

    @Step("<key> id'li elemente double click yapılması")
    public void doubleClick(String key){
       /*
        Actions actions = new Actions(appiumDriver);
        MobileElement appiumElement=appiumDriver.findElement(By.id(key));
        actions.moveToElement(appiumElement);
        actions.doubleClick(appiumElement);
        actions.perform();
    */
        appiumDriver.findElement(By.id(key)).click();
        appiumDriver.findElement(By.id(key)).click();

    }


}
