// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides a Cognito User Identity Provider resource.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = new aws.cognito.UserPool("example", {
 *     autoVerifiedAttributes: ["email"],
 * });
 * const exampleProvider = new aws.cognito.IdentityProvider("exampleProvider", {
 *     attributeMapping: {
 *         email: "email",
 *         username: "sub",
 *     },
 *     providerDetails: {
 *         authorize_scopes: "email",
 *         client_id: "your clientId",
 *         client_secret: "your clientSecret",
 *     },
 *     providerName: "Google",
 *     providerType: "Google",
 *     userPoolId: example.id,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_provider.html.markdown.
 */
export class IdentityProvider extends pulumi.CustomResource {
    /**
     * Get an existing IdentityProvider resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IdentityProviderState, opts?: pulumi.CustomResourceOptions): IdentityProvider {
        return new IdentityProvider(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:cognito/identityProvider:IdentityProvider';

    /**
     * Returns true if the given object is an instance of IdentityProvider.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is IdentityProvider {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === IdentityProvider.__pulumiType;
    }

    /**
     * The map of attribute mapping of user pool attributes. [AttributeMapping in AWS API documentation](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping)
     */
    public readonly attributeMapping!: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * The list of identity providers.
     */
    public readonly idpIdentifiers!: pulumi.Output<string[] | undefined>;
    /**
     * The map of identity details, such as access token
     */
    public readonly providerDetails!: pulumi.Output<{[key: string]: any}>;
    /**
     * The provider name
     */
    public readonly providerName!: pulumi.Output<string>;
    /**
     * The provider type.  [See AWS API for valid values](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType)
     */
    public readonly providerType!: pulumi.Output<string>;
    /**
     * The user pool id
     */
    public readonly userPoolId!: pulumi.Output<string>;

    /**
     * Create a IdentityProvider resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IdentityProviderArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: IdentityProviderArgs | IdentityProviderState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as IdentityProviderState | undefined;
            inputs["attributeMapping"] = state ? state.attributeMapping : undefined;
            inputs["idpIdentifiers"] = state ? state.idpIdentifiers : undefined;
            inputs["providerDetails"] = state ? state.providerDetails : undefined;
            inputs["providerName"] = state ? state.providerName : undefined;
            inputs["providerType"] = state ? state.providerType : undefined;
            inputs["userPoolId"] = state ? state.userPoolId : undefined;
        } else {
            const args = argsOrState as IdentityProviderArgs | undefined;
            if (!args || args.providerDetails === undefined) {
                throw new Error("Missing required property 'providerDetails'");
            }
            if (!args || args.providerName === undefined) {
                throw new Error("Missing required property 'providerName'");
            }
            if (!args || args.providerType === undefined) {
                throw new Error("Missing required property 'providerType'");
            }
            if (!args || args.userPoolId === undefined) {
                throw new Error("Missing required property 'userPoolId'");
            }
            inputs["attributeMapping"] = args ? args.attributeMapping : undefined;
            inputs["idpIdentifiers"] = args ? args.idpIdentifiers : undefined;
            inputs["providerDetails"] = args ? args.providerDetails : undefined;
            inputs["providerName"] = args ? args.providerName : undefined;
            inputs["providerType"] = args ? args.providerType : undefined;
            inputs["userPoolId"] = args ? args.userPoolId : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(IdentityProvider.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering IdentityProvider resources.
 */
export interface IdentityProviderState {
    /**
     * The map of attribute mapping of user pool attributes. [AttributeMapping in AWS API documentation](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping)
     */
    readonly attributeMapping?: pulumi.Input<{[key: string]: any}>;
    /**
     * The list of identity providers.
     */
    readonly idpIdentifiers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The map of identity details, such as access token
     */
    readonly providerDetails?: pulumi.Input<{[key: string]: any}>;
    /**
     * The provider name
     */
    readonly providerName?: pulumi.Input<string>;
    /**
     * The provider type.  [See AWS API for valid values](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType)
     */
    readonly providerType?: pulumi.Input<string>;
    /**
     * The user pool id
     */
    readonly userPoolId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a IdentityProvider resource.
 */
export interface IdentityProviderArgs {
    /**
     * The map of attribute mapping of user pool attributes. [AttributeMapping in AWS API documentation](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping)
     */
    readonly attributeMapping?: pulumi.Input<{[key: string]: any}>;
    /**
     * The list of identity providers.
     */
    readonly idpIdentifiers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The map of identity details, such as access token
     */
    readonly providerDetails: pulumi.Input<{[key: string]: any}>;
    /**
     * The provider name
     */
    readonly providerName: pulumi.Input<string>;
    /**
     * The provider type.  [See AWS API for valid values](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType)
     */
    readonly providerType: pulumi.Input<string>;
    /**
     * The user pool id
     */
    readonly userPoolId: pulumi.Input<string>;
}
