/**
 * boilerpipe
 *
 * Copyright (c) 2009 Christian Kohlschütter
 *
 * The author licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package de.l3s.boilerpipe.demo;

import java.net.URL;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.BufferedWriter;

import de.l3s.boilerpipe.extractors.ArticleExtractor;
import de.l3s.boilerpipe.extractors.CommonExtractors;
import de.l3s.boilerpipe.extractors.DefaultExtractor;


/**
 * Demonstrates how to use Boilerpipe to get the main content as plain text.
 * Note: In real-world cases, you'd probably want to download the file first using a fault-tolerant crawler.
 * 
 * @author Christian Kohlschütter
 * @see HTMLHighlightDemo if you need HTML as well.
 */
public class Html2txt {

    public static void main(final String[] args) throws Exception {
    
        // read from the url list file and handle one url each run
        BufferedReader in = new BufferedReader(new FileReader("./urls.txt"));
        String line;
        
        // flag for file names
        int i = 1;

        while ((line = in.readLine()) != null) {

            // url read from the input url list file
            // version without error handling:
            // final URL url = new URL(line);
            // version with error handling:
            URL url;            
            try {
                url = new URL(line);
            } catch (Exception e) {
                // Print out the exception that occurred
                System.out.println(line+": "+e.getMessage());
                i += 1;
                continue;
            }

            // write to file part for each run 
            FileWriter fstream = new FileWriter("./output/"+i+".txt");
            BufferedWriter out = new BufferedWriter(fstream);
            
            // write text back to the file
            // version without error handling:
            // out.write(DefaultExtractor.INSTANCE.getText(url));
            // out.write(ArticleExtractor.INSTANCE.getText(url));
            // out.write(CommonExtractors.CANOLA_EXTRACTOR.getText(url));
            // version with error handling:
            try {
                // out.write(DefaultExtractor.INSTANCE.getText(url));
                out.write(ArticleExtractor.INSTANCE.getText(url));
                // out.write(CommonExtractors.CANOLA_EXTRACTOR.getText(url));
            } catch (Exception e) {
                // Print out the exception that occurred
                System.out.println(line+": "+e.getMessage());
                out.close();
                i += 1;
                continue;
            }            

            // close the output stream
            out.close();

            System.out.println(i);

            // increase file number
            i += 1;

        }

        // finally, close the input url list file
        in.close();
        System.out.println("Done!");

    }
}
