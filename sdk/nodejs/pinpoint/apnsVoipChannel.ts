// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a Pinpoint APNs VoIP Channel resource.
 * 
 * > **Note:** All arguments, including certificates and tokens, will be stored in the raw state as plain-text.
 * [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * import * as fs from "fs";
 * 
 * const app = new aws.pinpoint.App("app", {});
 * const apnsVoip = new aws.pinpoint.ApnsVoipChannel("apnsVoip", {
 *     applicationId: app.applicationId,
 *     certificate: fs.readFileSync("./certificate.pem", "utf-8"),
 *     privateKey: fs.readFileSync("./private_key.key", "utf-8"),
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/pinpoint_apns_voip_channel.markdown.
 */
export class ApnsVoipChannel extends pulumi.CustomResource {
    /**
     * Get an existing ApnsVoipChannel resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApnsVoipChannelState, opts?: pulumi.CustomResourceOptions): ApnsVoipChannel {
        return new ApnsVoipChannel(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:pinpoint/apnsVoipChannel:ApnsVoipChannel';

    /**
     * Returns true if the given object is an instance of ApnsVoipChannel.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ApnsVoipChannel {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ApnsVoipChannel.__pulumiType;
    }

    /**
     * The application ID.
     */
    public readonly applicationId!: pulumi.Output<string>;
    /**
     * The ID assigned to your iOS app. To find this value, choose Certificates, IDs & Profiles, choose App IDs in the Identifiers section, and choose your app.
     */
    public readonly bundleId!: pulumi.Output<string | undefined>;
    /**
     * The pem encoded TLS Certificate from Apple.
     */
    public readonly certificate!: pulumi.Output<string | undefined>;
    /**
     * The default authentication method used for APNs. 
     * __NOTE__: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
     * You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
     * If your default authentication type fails, Amazon Pinpoint doesn't attempt to use the other authentication type.
     */
    public readonly defaultAuthenticationMethod!: pulumi.Output<string | undefined>;
    /**
     * Whether the channel is enabled or disabled. Defaults to `true`.
     */
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    /**
     * The Certificate Private Key file (ie. `.key` file).
     */
    public readonly privateKey!: pulumi.Output<string | undefined>;
    /**
     * The ID assigned to your Apple developer account team. This value is provided on the Membership page.
     */
    public readonly teamId!: pulumi.Output<string | undefined>;
    /**
     * The `.p8` file that you download from your Apple developer account when you create an authentication key. 
     */
    public readonly tokenKey!: pulumi.Output<string | undefined>;
    /**
     * The ID assigned to your signing key. To find this value, choose Certificates, IDs & Profiles, and choose your key in the Keys section.
     */
    public readonly tokenKeyId!: pulumi.Output<string | undefined>;

    /**
     * Create a ApnsVoipChannel resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ApnsVoipChannelArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ApnsVoipChannelArgs | ApnsVoipChannelState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ApnsVoipChannelState | undefined;
            inputs["applicationId"] = state ? state.applicationId : undefined;
            inputs["bundleId"] = state ? state.bundleId : undefined;
            inputs["certificate"] = state ? state.certificate : undefined;
            inputs["defaultAuthenticationMethod"] = state ? state.defaultAuthenticationMethod : undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["privateKey"] = state ? state.privateKey : undefined;
            inputs["teamId"] = state ? state.teamId : undefined;
            inputs["tokenKey"] = state ? state.tokenKey : undefined;
            inputs["tokenKeyId"] = state ? state.tokenKeyId : undefined;
        } else {
            const args = argsOrState as ApnsVoipChannelArgs | undefined;
            if (!args || args.applicationId === undefined) {
                throw new Error("Missing required property 'applicationId'");
            }
            inputs["applicationId"] = args ? args.applicationId : undefined;
            inputs["bundleId"] = args ? args.bundleId : undefined;
            inputs["certificate"] = args ? args.certificate : undefined;
            inputs["defaultAuthenticationMethod"] = args ? args.defaultAuthenticationMethod : undefined;
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["privateKey"] = args ? args.privateKey : undefined;
            inputs["teamId"] = args ? args.teamId : undefined;
            inputs["tokenKey"] = args ? args.tokenKey : undefined;
            inputs["tokenKeyId"] = args ? args.tokenKeyId : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ApnsVoipChannel.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ApnsVoipChannel resources.
 */
export interface ApnsVoipChannelState {
    /**
     * The application ID.
     */
    readonly applicationId?: pulumi.Input<string>;
    /**
     * The ID assigned to your iOS app. To find this value, choose Certificates, IDs & Profiles, choose App IDs in the Identifiers section, and choose your app.
     */
    readonly bundleId?: pulumi.Input<string>;
    /**
     * The pem encoded TLS Certificate from Apple.
     */
    readonly certificate?: pulumi.Input<string>;
    /**
     * The default authentication method used for APNs. 
     * __NOTE__: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
     * You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
     * If your default authentication type fails, Amazon Pinpoint doesn't attempt to use the other authentication type.
     */
    readonly defaultAuthenticationMethod?: pulumi.Input<string>;
    /**
     * Whether the channel is enabled or disabled. Defaults to `true`.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * The Certificate Private Key file (ie. `.key` file).
     */
    readonly privateKey?: pulumi.Input<string>;
    /**
     * The ID assigned to your Apple developer account team. This value is provided on the Membership page.
     */
    readonly teamId?: pulumi.Input<string>;
    /**
     * The `.p8` file that you download from your Apple developer account when you create an authentication key. 
     */
    readonly tokenKey?: pulumi.Input<string>;
    /**
     * The ID assigned to your signing key. To find this value, choose Certificates, IDs & Profiles, and choose your key in the Keys section.
     */
    readonly tokenKeyId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ApnsVoipChannel resource.
 */
export interface ApnsVoipChannelArgs {
    /**
     * The application ID.
     */
    readonly applicationId: pulumi.Input<string>;
    /**
     * The ID assigned to your iOS app. To find this value, choose Certificates, IDs & Profiles, choose App IDs in the Identifiers section, and choose your app.
     */
    readonly bundleId?: pulumi.Input<string>;
    /**
     * The pem encoded TLS Certificate from Apple.
     */
    readonly certificate?: pulumi.Input<string>;
    /**
     * The default authentication method used for APNs. 
     * __NOTE__: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
     * You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
     * If your default authentication type fails, Amazon Pinpoint doesn't attempt to use the other authentication type.
     */
    readonly defaultAuthenticationMethod?: pulumi.Input<string>;
    /**
     * Whether the channel is enabled or disabled. Defaults to `true`.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * The Certificate Private Key file (ie. `.key` file).
     */
    readonly privateKey?: pulumi.Input<string>;
    /**
     * The ID assigned to your Apple developer account team. This value is provided on the Membership page.
     */
    readonly teamId?: pulumi.Input<string>;
    /**
     * The `.p8` file that you download from your Apple developer account when you create an authentication key. 
     */
    readonly tokenKey?: pulumi.Input<string>;
    /**
     * The ID assigned to your signing key. To find this value, choose Certificates, IDs & Profiles, and choose your key in the Keys section.
     */
    readonly tokenKeyId?: pulumi.Input<string>;
}
